#!/bin/bash

if [ ! -f ~/.config/configuracionPuerto.cfg ]; then
 output="$(xrandr | grep " connected" | awk '{print$1}')"
else
 output=$(head -n 1 ~/.config/configuracionPuerto.cfg)
fi

xrandr --output $output --mode "640x240x60.00"

/usr/bin/PCSX2 --nogui --fullscreen "$@" &

BACK_PID=$!
wait $BACK_PID

xrandr --output $output --mode "700x480_59.94"






