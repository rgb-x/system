#!/bin/bash

###############################################################################################################
#Script para la el lanzamiento desde un FrontEnd de una rom con RetroArch en Pixel Perfect                    #
###############################################################################################################

#Ruta al fichero de configuración dinamico.1. AQUI DEBES INDICAR LA RUTA DONDE VAS A DEJAR EL FICHERO DE CONFGIURACIÓN DINAMICA
CONFIG_FILE="$HOME/.mame/mame.ini"
sed -i 's/\(orientation               *\).*/\1vertical/' $CONFIG_FILE
sed -i 's/\(sleep                     *\).*/\10/' $CONFIG_FILE

#Cogemos el puerto
if [ ! -f ~/.config/configuracionPuerto.cfg ]; then
	output="$(xrandr | grep " connected" | awk '{print$1}')"
else
	output=$(head -n 1 ~/.config/configuracionPuerto.cfg)
fi

#Obtengo el tipo de monitor del usuario
if [ ! -f ~/.config/configuracionMonitor.cfg ]; then
	monitor  = "Horizontal"
else
	monitor=$(head -n 1 ~/.config/configuracionMonitor.cfg)
fi

xrandr --output $output --mode "648x480x60.00"

if [[ $monitor == "Auto. Izquierda" ]]; then
	xrandr -o left
fi

if [[ $monitor == "Auto. Derecha" ]]; then
	xrandr -o right
fi

if [[ $monitor == "Vertical. Izquierda" ]]; then
	xrandr -o left
fi

if [[ $monitor == "Vertical. Derecha" ]]; then
	xrandr -o right
fi
	
#Cargamos la rom añadiendo la configuración dinamica.3.CAMBIA LA RUTA AL MOTOR, FICHERO DE CONFIGURACIÓN DINAMICA Y ROMS EN BASE A TUS RUTAS
$HOME/.mame/groovymame "$@" &
BACK_PID=$!
wait $BACK_PID

xrandr -o normal
xrandr --output $output --mode "700x480_59.94"

if [[ $monitor == "Vertical. Izquierda" ]]; then
	xrandr -o left
fi

if [[ $monitor == "Vertical. Derecha" ]]; then
	xrandr -o right
fi
