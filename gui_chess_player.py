import time
import os
import subprocess
import tkinter as tk
import sys
import urllib.request
import customtkinter as ctk

# Read resolution arguments injected by the shell launcher script
if len(sys.argv) == 3:
    COLS = int(sys.argv[1])
    ROWS = int(sys.argv[2])
else:
    # Default fallback quality setting
    COLS, ROWS = 80, 40

FPS = 30
FRAME_DURATION = 1.0 / FPS

WORKSPACE = os.path.expanduser("~/chess_frames")
os.makedirs(WORKSPACE, exist_ok=True)
VIDEO_PATH = os.path.join(WORKSPACE, "bad_apple_core.mp4")
AUDIO_OUT = os.path.join(WORKSPACE, "runtime_audio.wav")

VIDEO_MIRROR_URL = "https://wikimedia.org"

def verify_and_fetch_assets():
    local_backups = [
        os.path.expanduser("~/chess_frames/bad_apple_new.mp4"),
        os.path.join(os.getcwd(), "bad_apple_new.mp4"),
        os.path.expanduser("~/bad_apple_new.mp4"),
        os.path.expanduser("~/chess_frames/bad_apple_core.mp4")
    ]
    
    for backup in local_backups:
        if os.path.exists(backup) and os.path.getsize(backup) > 1000000:
            print(f"[ Local asset detected at: {backup} ]")
            global VIDEO_PATH
            VIDEO_PATH = backup
            return

    if not os.path.exists(VIDEO_PATH) or os.path.getsize(VIDEO_PATH) < 1000000:
        print("\n[ INITIALIZING FIRST-TIME STARTUP ENVIRONMENT ]")
        print("Downloading verified Bad Apple!! source file stream container...")
        print("Please wait a moment (this only happens once)...")
        try:
            req = urllib.request.Request(VIDEO_MIRROR_URL, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(VIDEO_PATH, 'wb') as out_file:
                out_file.write(response.read())
            print("Download Complete! Storage synchronized securely.")
        except Exception as e:
            print(f"\n[ NETWORK ERROR: Failed to pull asset mirror ({e}) ]")
            sys.exit(1)

verify_and_fetch_assets()

print(f"Pre-loading {COLS}x{ROWS} chess video containers into memory...")
subprocess.run(["ffmpeg", "-y", "-i", VIDEO_PATH, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", AUDIO_OUT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

ffmpeg_process = subprocess.Popen([
    "ffmpeg", "-y", "-i", VIDEO_PATH,
    "-an", "-vf", f"fps=30,scale={COLS}:{ROWS}:flags=neighbor,format=gray", 
    "-f", "image2pipe", "-vcodec", "rawvideo", "-"
], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

PRELOADED_FRAMES = []
while True:
    raw_bytes = ffmpeg_process.stdout.read(COLS * ROWS)
    if not raw_bytes or len(raw_bytes) < (COLS * ROWS):
        break
    
    frame_matrix = []
    for y in range(ROWS):
        row_start = y * COLS
        row_bytes = raw_bytes[row_start : row_start + COLS]
        frame_matrix.append(list(row_bytes))
    PRELOADED_FRAMES.append(frame_matrix)

ffmpeg_process.stdout.close()
ffmpeg_process.wait()

print(f"Cached {len(PRELOADED_FRAMES)} animation layers. Booting engine...")

if len(PRELOADED_FRAMES) == 0:
    print("\n[ ERROR: FFmpeg data parsing loop returned an empty stream layout. ]\n")
    sys.exit(1)

ctk.set_appearance_mode("Dark")

class BadAppleChessPlayer:
    def __init__(self, root):
        self.root = root
        self.frames = PRELOADED_FRAMES
        self.total_frames = len(self.frames)
        self.audio_process = None
        self.start_time = 0
        self.is_fullscreen = False
        
        self.canvas = tk.Canvas(root, bg="#ebd0b9", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        try:
            self.audio_process = subprocess.Popen(["paplay", AUDIO_OUT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Audio sound card initialization error: {e}")

        self.root.bind("<F11>", self.toggle_fullscreen)
        self.root.bind("<f>", self.toggle_fullscreen)

        self.start_time = time.time()
        self.update_engine_loop()

    def toggle_fullscreen(self, event=None):
        self.is_fullscreen = not self.is_fullscreen
        self.root.attributes("-fullscreen", self.is_fullscreen)
        return "break"

    def update_engine_loop(self):
        elapsed_time = time.time() - self.start_time
        target_frame = int(elapsed_time / FRAME_DURATION)
        
        if target_frame >= self.total_frames:
            self.close_application()
            return

        win_width = self.canvas.winfo_width()
        win_height = self.canvas.winfo_height()
        
        if win_width <= 1 or win_height <= 1:
            win_width, win_height = 960, 480

        cell_w = win_width / COLS
        cell_h = win_height / ROWS
        font_size = max(3, int(cell_h * 0.70))

        self.canvas.delete("all")
        current_frame = self.frames[target_frame]
        
        for y_idx in range(ROWS):
            for x_idx in range(COLS):
                x1 = int(x_idx * cell_w)
                y1 = y_idx * cell_h
                x2 = int((x_idx + 1) * cell_w)
                y2 = (y_idx + 1) * cell_h
                
                cx = (x1 + x2) // 2
                cy = int((y1 + y2) // 2)
                
                tile_color = "#ebd0b9" if (x_idx + y_idx) % 2 == 0 else "#b58863"
                self.canvas.create_rectangle(x1, int(y1), x2, int(y2), fill=tile_color, outline="")
                
                if current_frame[y_idx][x_idx] > 127:
                    self.canvas.create_text(cx, cy, text="♔", fill="#fafaf9", font=("Arial", font_size))
                else:
                    self.canvas.create_text(cx, cy, text="♚", fill="#1c1917", font=("Arial", font_size, "bold"))

        self.root.after(12, self.update_engine_loop)

    def close_application(self, event=None):
        if self.audio_process:
            try: self.audio_process.terminate()
            except: pass
        self.root.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Bad Apple!! - Multi-Resolution Chess Player")
    root.geometry("1100x600")
    root.resizable(True, True)
    
    app = BadAppleChessPlayer(root)
    
    root.protocol("WM_DELETE_WINDOW", app.close_application)
    root.bind("<Escape>", lambda e: app.close_application())
    root.mainloop()
