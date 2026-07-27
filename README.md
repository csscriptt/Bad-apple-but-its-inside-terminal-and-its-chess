# Bad Apple - Chess Display

Plays the Bad Apple video inside a window using chess pieces. Supports Linux and Windows.

## Installation & Setup

1. Clone: `git clone https://github.com`
2. Navigate: `cd Bad-apple-but-its-inside-terminal-and-its-chess`
3. Install Deps: `pip install -r requirements.txt`
4. Run: `python gui_chess_player.py`

### Dependencies
*   **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install -y ffmpeg python3-tk`
*   **Windows:** Install Python 3 & FFmpeg (add to PATH).

---

## Troubleshooting Guide

1.  **Error: "No module named tkinter"**
    *   `sudo apt install python3-tk -y` (Linux)
2.  **Error: "externally-managed-environment"**
    *   `pip install -r requirements.txt --break-system-packages`
3.  **Video/Audio Issues**
    *   Run: `pkill -9 paplay && pkill -9 ffmpeg`
