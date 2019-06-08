#!/bin/bash

###############################################################################################################
#Script para la el lanzamiento desde un FrontEnd de una juego con ppsspp                  #
###############################################################################################################
if [ ! -f ~/.config/configuracionPuerto.cfg ]; then
 output="$(xrandr | grep " connected" | awk '{print$1}')"
else
 output=$(head -n 1 ~/.config/configuracionPuerto.cfg)
fi

 xrandr --output $output --mode "648x480x60.00"
/usr/bin/ppsspp "$@" &
BACK_PID=$!
wait $BACK_PID

xrandr --output $output --mode "700x480_59.94"


