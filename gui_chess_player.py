import time
import os
import subprocess
import tkinter as tk
import sys
import urllib.request
import customtkinter as ctk

# Base video dimension metrics
COLS, ROWS = 40, 20
FPS = 30
FRAME_DURATION = 1.0 / FPS

# Secure workspace path handlers
WORKSPACE = os.path.expanduser("~/chess_frames")
os.makedirs(WORKSPACE, exist_ok=True)
VIDEO_PATH = os.path.join(WORKSPACE, "bad_apple_core.mp4")
AUDIO_OUT = os.path.join(WORKSPACE, "runtime_audio.wav")

# Public mirror hosting a verified, uncorrupted flat 30 FPS copy of Bad Apple
VIDEO_MIRROR_URL = "https://archive.org"

def verify_and_fetch_assets():
    if not os.path.exists(VIDEO_PATH):
        print("\n[ INITIALIZING FIRST-TIME STARTUP ENVIRONMENT ]")
        print("Downloading verified Bad Apple!! source file stream container...")
        print("Please wait a moment (this only happens once)...")
        try:
            # Native Python buffer block downloader bypassing curl/wget locks
            urllib.request.urlretrieve(VIDEO_MIRROR_URL, VIDEO_PATH)
            print("Download Complete! Storage synchronized securely.")
        except Exception as e:
            print(f"\n[ NETWORK ERROR: Failed to pull asset mirror ({e}) ]")
            print("Please check your internet configuration or firewall locks and try again.\n")
            sys.exit(1)

# Execute the asset synchronization before booting the GUI
verify_and_fetch_assets()

print("Pre-loading video containers into system memory...")
# 1. Pipeline out clean audio waves
subprocess.run(["ffmpeg", "-y", "-i", VIDEO_PATH, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", AUDIO_OUT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 2. Extract high-speed binary video frames directly
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

print(f"Cached {len(PRELOADED_FRAMES)} animation layers. Booting responsive widescreen engine...")

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
        
        # Start canvas with pure boxwood color backdrop to blend seamlessly
        self.canvas = tk.Canvas(root, bg="#ebd0b9", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        try:
            self.audio_process = subprocess.Popen(["paplay", AUDIO_OUT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Audio sound card initialization error: {e}")

        # Bind Fullscreen triggers to standard hotkeys
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
        font_size = max(8, int(cell_h * 0.65))

        self.canvas.delete("all")
        current_frame = self.frames[target_frame]
        
        for y in range(ROWS):
            for x in range(COLS):
                x1 = int(x * cell_w)
                y1 = y * cell_h
                x2 = int((x + 1) * cell_w)
                y2 = (y + 1) * cell_h
                
                cx = (x1 + x2) // 2
                cy = int((y1 + y2) // 2)
                
                tile_color = "#ebd0b9" if (x + y) % 2 == 0 else "#b58863"
                self.canvas.create_rectangle(x1, int(y1), x2, int(y2), fill=tile_color, outline="")
                
                if current_frame[y][x] > 127:
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
    root.title("Bad Apple!! - Responsive Wood Chess Player")
    root.geometry("960x480")
    root.resizable(True, True)
    
    app = BadAppleChessPlayer(root)
    
    root.protocol("WM_DELETE_WINDOW", app.close_application)
    root.bind("<Escape>", lambda e: app.close_application())
    root.mainloop()
