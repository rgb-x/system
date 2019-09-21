#!/bin/bash

# escribid los scripts para que los tabuladores los convierta en 4 espacios.

# inicializaciones de paths, imprescindibles
# las variables de entorno son generadas por rgbux-env
. /opt/RGBux/bin/system-base

# contiene funciones de ayuda, como los replace
. /opt/RGBux/bin/rgbux-helpers

# como hemos podido variar la variable de entorno pero sin reiniciar, 
# machacamos el env actual volviendo a leer CFG_SYSTEM
. $CFG_SYSTEM

# ACCIONES


# FUNCIONES BASE

# $1 contiene el puerto DRM (Ej: DVI-I-1)
function runcmd()
{
   # esta funcion esta en rgbux-env, pasa de formato DRM a X11 (Ej: DVI-0)
    DRM_PT=$1
    XORG_PT=$(x11_getdrm "$DRM_PT")
    #echo $XORG_PT
    set_port $XORG_PT $DRM_PT
}

function print_opts()
{
    echo $PORTS_DRM
}

function print_current()
{
    echo $CONNECTOR_DRM
}

case $1 in
    current)
        print_current
        ;;
    info)
        print_opts
        ;;
    run)
        runcmd $2
        ;;
    *)
        echo "$0: [run|info|current]"
        ;;
esac

