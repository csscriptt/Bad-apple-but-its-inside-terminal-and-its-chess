# Bad Apple - Chess Display

Plays the Bad Apple video inside a window using chess pieces. Supports Linux and Windows.

## Installation & Setup

Ensure Python 3 and FFmpeg are installed, then run:

```bash
git clone https://github.com
cd Bad-apple-but-its-inside-terminal-and-its-chess
pip install -r requirements.txt
python gui_chess_player.py
```

### System-Specific Dependencies
*   **Arch/Manjaro:** `sudo pacman -S ffmpeg tk pulseaudio-utils --needed`
*   **Ubuntu/Debian/Mint:** `sudo apt update && sudo apt install -y ffmpeg python3-tk pulseaudio-utils`
*   **Fedora/RHEL:** `sudo dnf install -y ffmpeg python3-tkinter`
*   **Windows:** Install Python 3 (add to PATH) and FFmpeg (add to PATH).

---

## Controls
*   **F11/F**: Toggle Fullscreen
*   **Esc**: Exit

---

## Troubleshooting

*   **Blank Window/Frozen Video:** Run `pkill -9 paplay && pkill -9 ffmpeg && rm -rf ~/chess_frames/` to clear cache and processes.
*   **`pip` Error (Linux):** Add `--break-system-packages` to the `pip` command.
*   **ModuleNotFoundError: 'tkinter':** Install via system package manager (e.g., `python3-tk` or `tk`).
*   **Audio Lags:** Ensure `pulseaudio-utils` is installed for proper pipewire/pulse handling.
