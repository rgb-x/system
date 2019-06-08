#!/bin/bash

if [ ! -f ~/.config/configuracionMonitor.cfg ]; then
    ~/.config/Verticales.sh
else
    line=$(head -n 1 ~/.config/configuracionMonitor.cfg)
    
    case `echo "$line"` in
    "$(echo $line | grep 'Horizontal')")
	xrandr -o normal
	#feh --bg-scale ~/wallpaper/cartel.png
	if [ -e ~/.config/MonitorCambiado.cfg ]; then
		rm ~/.emulationstation/es_settings.cfg
		cp ~/.emulationstation/es_settings_H.cfg ~/.emulationstation/es_settings.cfg
		rm ~/.config/MonitorCambiado.cfg

	fi
	;;
    "$(echo $line | grep 'Vertical. Derecha')")
	xrandr -o right
	#feh --bg-scale ~/wallpaper/"vertical.png"
	if [ -e ~/.config/MonitorCambiado.cfg ]; then
		rm ~/.emulationstation/es_settings.cfg
		cp ~/.emulationstation/es_settings_V.cfg ~/.emulationstation/es_settings.cfg
		rm ~/.config/MonitorCambiado.cfg
	fi
	;;
    "$(echo $line | grep 'Vertical. Izquierda')")
	xrandr -o left
	#feh --bg-scale ~/wallpaper/"vertical.png"
	if [ -e ~/.config/MonitorCambiado.cfg ]; then
		rm ~/.emulationstation/es_settings.cfg
		cp ~/.emulationstation/es_settings_V.cfg ~/.emulationstation/es_settings.cfg
		rm ~/.config/MonitorCambiado.cfg
	fi
	;;
    *)
	xrandr -o normal
	#feh --bg-scale ~/wallpaper/cartel.png
	if [ -e ~/.config/MonitorCambiado.cfg ]; then
		rm ~/.emulationstation/es_settings.cfg
		cp ~/.emulationstation/es_settings_H.cfg ~/.emulationstation/es_settings.cfg
		rm ~/.config/MonitorCambiado.cfg
	fi
	;;
    esac

	#Solo cuando el usuario tenga la tarjeta configurada entremos en modo arcade
	if [ -e ~/.config/configuracionTarjeta.cfg ]; then
		xset dpms 0 0 0
    		xset -dpms
    		xset s noblank
    		xset s noexpose
    		xset s 0 0
		sleep 5
		~/EmulationStation/emulationstation.sh
	fi
fi