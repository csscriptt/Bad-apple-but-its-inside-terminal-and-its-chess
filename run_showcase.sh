#!/bin/bash
clear
echo "===================================================="
echo "       CHESSBOARD VIDEO SYNTHESIS ENGINE v1.2       "
echo "===================================================="
echo "Select Video Render Quality Layer Level:"
echo "  1) Low Density Quality  - 40x20  (800 Tiles)"
echo "  2) Medium HD Quality    - 80x40  (3,200 Tiles)"
echo "  3) Ultra Max HD Quality - 160x80 (12,800 Tiles)"
echo "===================================================="
read -p "Enter choice (1-3): " CHOICE

case $CHOICE in
    1) COLS=40; ROWS=20 ;;
    2) COLS=80; ROWS=40 ;;
    3) COLS=160; ROWS=80 ;;
    *) echo "Invalid input selection. Using 80x40 fallback default."; COLS=80; ROWS=40 ;;
esac

echo ""
echo "[+] Resolution Configuration Target Lock: ${COLS}x${ROWS}"
echo "Starting YouTube Showcase Recording countdown..."

for i in 3 2 1; do
    echo "  [ $i ] "
    sleep 1
done

clear
pkill -9 paplay &>/dev/null
pkill -9 ffmpeg &>/dev/null

# Launch with injected command line quality arguments
python gui_chess_player.py $COLS $ROWS &
PLAYER_PID=$!

sleep 1.5
if command -v xdotool &> /dev/null; then
    xdotool key F11
elif command -v ydotool &> /dev/null; then
    ydotool key F11
fi

wait $PLAYER_PID
