# Bad Apple - Wood Chess Player

This program plays the Bad Apple video inside a window using changing chess board squares and chess pieces. It works on both Linux and Windows computers.

## Requirements

You need to have Python and FFmpeg installed on your computer.

### Linux Package Installation

Run the command for your specific Linux distribution:

```bash
# For Arch Linux / Manjaro
sudo pacman -S ffmpeg tk --needed

# For Ubuntu / Debian / Pop!_OS / Mint
sudo apt update && sudo apt install -y ffmpeg python3-tk

# For Fedora / RHEL
sudo dnf install -y ffmpeg python3-tkinter
```

### Windows Users
Make sure you have downloaded Python from python.org (check the box to "Add Python to PATH" during setup) and installed FFmpeg.

## How to Install and Run

Open your terminal or command prompt and run these commands in order:

```bash
# 1. Download the code files
git clone https://github.com
cd Bad-apple-but-its-inside-terminal-and-its-chess

# 2. Install the required window package
pip install -r requirements.txt

# 3. Run the player program
python gui_chess_player.py
```

*Note: If the second command fails on your system, try running it with the `--break-system-packages` flag.*

## Controls
* Press the **F11** key or the **F** key to toggle Fullscreen mode.
* Press the **Escape** key (Esc) to close the program completely.

## Troubleshooting (Common Bug Fixes)

If you run into an error when launching or running the program, look for your issue below:

### 1. Error: "paplay: command not found" or Silent Audio
The program uses your system sound server (`paplay`). If audio does not work, install your sound utilities:
```bash
# On Arch Linux
sudo pacman -S pulseaudio-utils --needed

# On Ubuntu / Debian
sudo apt install -y pulseaudio-utils
```

### 2. Error: "externally-managed-environment" when running pip
Modern Linux distros block global pip installs. Add the bypass flag:
```bash
pip install -r requirements.txt --break-system-packages
```

### 3. Error: "No module named tkinter" or Window fails to open
Your Python installation is missing its graphical user interface package. Fix it by running:
```bash
# On Arch Linux
sudo pacman -S tk --needed

# On Ubuntu / Debian
sudo apt install -y python3-tk

# On Fedora
sudo dnf install -y python3-tkinter
```

### 4. Video hangs or starts with an empty board cache
Old hardware threads or corrupted files might be locking up your media folders. Force-wipe the active cache:
```bash
pkill -9 paplay && pkill -9 ffmpeg && rm -rf ~/chess_frames/
```
