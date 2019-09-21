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

# FUNCIONES BASE

function runcmd()
{
    NEW_MONITOR=$1
    # para groovymame
    replace_mame "monitor" $NEW_MONITOR /etc/mame/mame.ini
    # la variable de entorno la usa switchres
    replace_value "MONITOR" $NEW_MONITOR $CFG_SYSTEM
    echo "New Value: ${NEW_MONITOR}, please restart system."
}

function print_opts()
{
    echo "generic_15|arcade_15|arcade_15ex|h9110|arcade_31|vesa_480|vesa_768"
}

function print_current()
{
    echo $MONITOR
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

