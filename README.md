# Bad Apple - Chess Display

Plays the Bad Apple video inside a window using chess pieces. Supports Linux and Windows.

## Installation & Setup

### Linux Users
```bash
git clone https://github.com/csscriptt/Bad-apple-but-its-inside-terminal-and-its-chess
cd Bad-apple-but-its-inside-terminal-and-its-chess
pip install -r requirements.txt --break-system-packages
python gui_chess_player.py
```

### Windows Users
1. **Install Python:** Add to PATH.
2. **Install Library:** `pip install customtkinter`
3. **Install FFmpeg:** Add `ffmpeg.exe` to `C:\Windows\System32\`.
4. **Run:** `python gui_chess_player.py`

---

## Prerequisites (Linux)
*   **Arch/Manjaro:** `sudo pacman -S ffmpeg tk opencv`
*   **Ubuntu/Debian/Mint:** `sudo apt install -y ffmpeg python3-tk`
*   **Fedora:** `sudo dnf install -y ffmpeg python3-tkinter`

---

## Troubleshooting
*   **Module Not Found:** Install `python3-tk` or `tk`.
*   **Frozen/No Audio:** `pkill -9 paplay && pkill -9 ffmpeg`
