# Bad Apple - Wood Chess Player

This program plays the Bad Apple video inside a window using changing chess board squares and chess pieces. It works on both Linux and Windows computers.

## Features
* Automatic Download: The program downloads the video file by itself the first time you run it. You do not need to download the video manually.
* Wood Colors: The board uses brown wood colors.
* Fullscreen Mode: The chess board grows or shrinks to fit your screen if you make the window bigger.
* Audio Sync: The music and the video frames stay timed together.

## Before You Start

You need to have Python and FFmpeg installed on your computer.

If you are on Arch Linux, install these packages first:
```bash
sudo pacman -S ffmpeg tk --needed
```

If you are on Windows, make sure you downloaded Python from python.org and installed FFmpeg.

## How to Install and Run

Open your terminal or command prompt and run these commands in order:

```bash
# 1. Download the code files from GitHub
git clone https://github.com
cd chess-bad-apple

# 2. Install the required window package
pip install -r requirements.txt --break-system-packages

# 3. Run the player program
python gui_chess_player.py
```

*Note for Windows users: If the second command fails, try running it without the `--break-system-packages` flag.*

## How to Control the Program
* Press the F11 key or the F key on your keyboard to go into Fullscreen mode.
* Press the Escape key (Esc) on your keyboard to close the program completely.
