# Bad Apple - Chess Display

Plays the Bad Apple video inside a window using changing chess board squares and chess pieces. It works on both Linux and Windows.

## Requirements

Python and FFmpeg are required.

### Installation

```bash
git clone https://github.com
cd Bad-apple-but-its-inside-terminal-and-its-chess
pip install -r requirements.txt
python gui_chess_player.py
```

## Linux Setup
Install ffmpeg and python-tk via your package manager (pacman, apt, or dnf).

## Troubleshooting
- **pip error:** Use `pip install -r requirements.txt --break-system-packages` on newer Linux distros.
- **tk module error:** Install `python3-tk` (Debian/Ubuntu) or `tk` (Arch).
- **No Audio:** Install `pulseaudio-utils`.
