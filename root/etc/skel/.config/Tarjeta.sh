#!/bin/bash
instalacion=$(zenity --list --title="Elije tu tipo de tarjeta:" --column="Marca" "ATI" "NVIDIA. Experimental" "INTEL. Experimental" --width=300 --height=200)

if [ -e ~/.config/configuracionMonitor.cfg ]; then
  rm ~/.config/configuracionTarjeta.cfg
  echo $instalacion > ~/.config/configuracionTarjeta.cfg 
else
  echo $instalacion > ~/.config/configuracionTarjeta.cfg 
fi

zenity --info --text="El sistema se reiniciará para finalizar la configuración" --width=400 --height=100
reboot