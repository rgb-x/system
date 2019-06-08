#!/bin/bash
instalacion=$(zenity --list   --title="Elije la instalación de tu monitor:" --column="Instalación" --column="Descripción" "Horizontal" "Podras jugar a juegos verticales con filtro bilinear. No tendrás pixel perfect" "Vertical. Derecha" "Si tienes un monitor en vertical girado a la derecha. No podras jugar a juegos horizontales" "Vertical. Izquierda" "Si tienes un monitor en vertical girado a la izquierda. No podras jugar a juegos horizontales" "Auto. Derecha" "El monitor gira automaticamente. Se puede jugar a juegos horizontales y verticales" "Auto. Izquierda" "El monitor gira automaticamente. Se puede jugar a juegos horizontales y verticales" --width=640 --height=200)
if [ -e ~/.config/configuracionMonitor.cfg ]; then
  rm ~/.config/configuracionMonitor.cfg
  echo $instalacion > ~/.config/configuracionMonitor.cfg
else
  echo $instalacion > ~/.config/configuracionMonitor.cfg 
fi

echo $instalacion > ~/.config/MonitorCambiado.cfg

zenity --info --text="El sistema se reiniciará para finalizar la configuración" --width=400 --height=100
reboot