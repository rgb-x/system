#!/bin/bash
#Obtengo el tipo de monitor del usuario
if [ ! -f ~/.config/configuracionMonitor.cfg ]; then
	monitor  = "Horizontal"
else
	monitor=$(head -n 1 ~/.config/configuracionMonitor.cfg)
fi

output="$(xrandr | grep " connected" | awk '{print$1}')"
retroarch  &
BACK_PID=$!
wait $BACK_PID
xrandr --output $output --mode "700x480_59.94"
if [[ $monitor == "Vertical. Izquierda" ]]; then
	xrandr -o left
fi
if [[ $monitor == "Vertical. Derecha" ]]; then
	xrandr -o right
fi

