#!/bin/bash

###############################################################################################################
#Script para la el lanzamiento desde un FrontEnd de una rom con RetroArch en Pixel Perfect                    #
###############################################################################################################

#Ruta al fichero de configuración dinamico.1. AQUI DEBES INDICAR LA RUTA DONDE VAS A DEJAR EL FICHERO DE CONFGIURACIÓN DINAMICA
CONFIG_FILE="$HOME/.retroarch/config/configuraciones/DinamicRetroarchAmstrad.cfg"

#Seteamos ruta de los saves
rutaLimpia=${@##*.so}
rutaLimpia=${rutaLimpia:3}
rutaSaves='/saves'
savesDir=$(dirname "$(dirname "$rutaLimpia")")$rutaSaves
mkdir -p "$savesDir"

#Modificamos el config dinámicamente
sed -i "s|\(savefile_directory *= *\).*|\1\""$savesDir"\"|" $CONFIG_FILE
sed -i 's/\(savefiles_in_content_dir *= *\).*/\1"false"/' $CONFIG_FILE
sed -i 's/\(savestate_auto_load *= *\).*/\1"true"/' $CONFIG_FILE
sed -i 's/\(savestate_auto_save *= *\).*/\1"true"/' $CONFIG_FILE
sed -i "s|\(savestate_directory *= *\).*|\1\""$savesDir"\"|" $CONFIG_FILE
sed -i 's/\(auto_overrides_enable *= *\).*/\1"false"/' $CONFIG_FILE

#Cogemos el puerto
if [ ! -f ~/.config/configuracionPuerto.cfg ]; then
	output="$(xrandr | grep " connected" | awk '{print$1}')"
else
	output=$(head -n 1 ~/.config/configuracionPuerto.cfg)
fi

#Obtengo el tipo de monitor del usuario
if [ ! -f ~/.config/configuracionMonitor.cfg ]; then
	monitor="Horizontal"
else
	monitor=$(head -n 1 ~/.config/configuracionMonitor.cfg)
fi

xrandr --output $output --mode "336x240x60.00"

#Cargamos la rom añadiendo la configuración dinamica.3.CAMBIA LA RUTA AL MOTOR, FICHERO DE CONFIGURACIÓN DINAMICA Y ROMS EN BASE A TUS RUTAS
retroarch --config $CONFIG_FILE "$@" &
BACK_PID=$!
wait $BACK_PID

xrandr --output $output --mode "700x480_59.94"
