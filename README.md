# Bad Apple - Chess Display

Plays the Bad Apple video inside a window using chess pieces. Supports Linux and Windows.

## Installation & Setup

### Linux Users
```bash
git clone https://github.com/csscriptt/Bad-apple-but-its-inside-terminal-and-its-chess/blob/main
cd Bad-apple-but-its-inside-terminal-and-its-chess
pip install -r requirements.txt --break-system-packages
python gui_chess_player.py
```

### Windows Users
1. Install Python (with "Add to PATH" checked).
2. Run `pip install customtkinter` in CMD.
3. Install FFmpeg and add `ffmpeg.exe` to system path.
4. Run `python gui_chess_player.py`.

## Prerequisites & Troubleshooting
Ensure you have `ffmpeg` and `tk` (tkinter) installed. If you encounter `externally-managed-environment` errors, use the `--break-system-packages` flag.

## Controls
*   **F11 / F:** Toggle Fullscreen
*   **Esc:** Close the program
