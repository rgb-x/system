#!/bin/bash

instalacion=$(zenity --entry --text "En algunos tipos de tarjeta no es posible capturar el puerto automaticamente.
Si no obtienes imagen en el CRT prueba a poner tu puerto a mano. 
Normalmente debe ser VGA-0, VGA-1, VGA0, VGA1... 
No hagas ningún cambio en este apartado si no estas seguro." --width=620 --height=200)

if [ -n "$instalacion" ]; then
  if [ -e ~/.config/configuracionPuerto.cfg ]; then
    rm ~/.config/configuracionPuerto.cfg
    echo $instalacion > ~/.config/configuracionPuerto.cfg
  else
    echo $instalacion > ~/.config/configuracionPuerto.cfg
  fi
fi