#!/bin/bash

###############################################################################################################
#Script para la el lanzamiento desde un FrontEnd de una rom con RetroArch en Pixel Perfect                    #
###############################################################################################################

#Ruta al fichero de configuración dinamico.1. AQUI DEBES INDICAR LA RUTA DONDE VAS A DEJAR EL FICHERO DE CONFGIURACIÓN DINAMICA
CONFIG_FILE="/home/arcade/.config/retroarch/config/configuraciones/DinamicRetroarchConsolaGba.cfg"
sed -i 's/\(auto_overrides_enable *= *\).*/\1"false"/' $CONFIG_FILE

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
	
#xrandr --output $output --mode "288x192x60.00"

#Cargamos la rom añadiendo la configuración dinamica.3.CAMBIA LA RUTA AL MOTOR, FICHERO DE CONFIGURACIÓN DINAMICA Y ROMS EN BASE A TUS RUTAS
retroarch -L /home/arcade/.config/retroarch/cores/mgba_libretro.so --config /home/arcade/.retroarch/config/configuraciones/DinamicRetroarchConsolaGba.cfg "$@" &
BACK_PID=$!
wait $BACK_PID

xrandr --output $output --mode "700x480_59.94"
