# Bad Apple - Chess Display

Plays the Bad Apple video inside a window using chess pieces. Supports Linux and Windows.

## Installation & Setup

### Linux Users
Open your terminal and run these commands in order:
```bash
# 1. Download the code
git clone https://github.com

# 2. Enter the folder
cd Bad-apple-but-its-inside-terminal-and-its-chess

# 3. Install requirements
pip install -r requirements.txt --break-system-packages

# 4. Run the player
python gui_chess_player.py
```

### Windows Users
Follow these steps:
1.  **Install Python:** Download from python.org. **Important:** Check "Add python.exe to PATH" during installation.
2.  **Install Library:** Open Command Prompt (`cmd`) and run: `pip install customtkinter`
3.  **Setup FFmpeg:** Download FFmpeg, extract it, and place `ffmpeg.exe` in `C:\Windows\System32\`.
4.  **Run:** Download the repo ZIP, extract it, open `cmd` in the folder, and run: `python gui_chess_player.py`

---

## Troubleshooting & Dependencies

*   **Linux Dependencies:** Install `ffmpeg` and `python3-tk` via your package manager (e.g., `sudo apt install -y ffmpeg python3-tk`).
*   **Errors:** If `customtkinter` is missing, run `pip install customtkinter`.
*   **Windows FFmpeg Error:** Re-check Step 3 above.

---

## Controls
*   **F11/F:** Toggle Fullscreen
*   **Esc:** Close
