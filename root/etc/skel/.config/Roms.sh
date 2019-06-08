#!/bin/bash

pass=$(zenity --password --text="Password sudo" --width=400 --height=100)

echo $pass | sudo -S chmod 777 -R /usr/local/games/roms
echo $pass | sudo -S ln -s /usr/local/games/roms ~/roms

zenity --info --text="Se han dado los permisos al directorio de ROMS" --width=400 --height=100