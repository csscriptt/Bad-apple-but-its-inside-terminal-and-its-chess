# Bad Apple - Chess Display

Plays the Bad Apple video inside a window using chess pieces. Supports Linux and Windows.

## Installation & Setup

### Linux Users
```bash
git clone https://github.com
cd Bad-apple-but-its-inside-terminal-and-its-chess
pip install -r requirements.txt --break-system-packages
python gui_chess_player.py
```

### Windows Users (Step-by-Step Guide)
1. **Install Python:** Go to python.org, download the installer, and ensure you check the box that says "Add python.exe to PATH" before clicking install.
2. **Install Library:** Open your Command Prompt (cmd) and run: `pip install customtkinter`
3. **Install FFmpeg:** Download FFmpeg for Windows, extract it, and copy the `ffmpeg.exe` file into your `C:\Windows\System32\` folder.
4. **Run:** Open Command Prompt inside your project folder and run: `python gui_chess_player.py`

---

## Linux Package Prerequisites
Run the exact command for your specific Linux distribution:
*   **Arch Linux / Manjaro:** `sudo pacman -S ffmpeg tk pulseaudio-utils --needed`
*   **Ubuntu / Debian / Mint:** `sudo apt update && sudo apt install -y ffmpeg python3-tk`
*   **Fedora:** `sudo dnf install -y ffmpeg python3-tkinter`

---

## Troubleshooting
*   **Error: "No module named tkinter"** -> Install your distro's GUI package listed in the prerequisites above (e.g., `python3-tk` or `tk`).
*   **Error: "externally-managed-environment"** -> Add the `--break-system-packages` flag to your pip command.
*   **Video freezes or Audio fails to start** -> Run this command to kill old background processes: `pkill -9 paplay && pkill -9 ffmpeg`

---

## Controls
*   **F11 / F:** Toggle Fullscreen
*   **Esc:** Close the program
