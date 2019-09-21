#!/bin/bash

# escribid los scripts para que los tabuladores los convierta en 4 espacios.

# inicializaciones de paths, imprescindibles
# las variables de entorno son generadas por rgbux-env
. /opt/RGBux/bin/system-base

# contiene funciones de ayuda, como los replace
. /opt/RGBux/bin/rgbux-helpers


# DATA BASE
DATA_FILE=$HOME/.mame/mame.ini
DATA_VAR="custom_difficulty"
DEFAULT_VALUE="default"

# FUNCIONES BASE
#custom_freeplay           0

function runcmd()
{
    value=$1
    # para groovymame
    replace_mame $DATA_VAR $value $DATA_FILE
    # la variable de entorno
    #replace_value "MONITOR" $NEW_MONITOR $CFG_SYSTEM
    echo "New Value: ${DATA_VAR} ${value}!"
}

function print_opts()
{
    echo "$DEFAULT_VALUE|easiest|easy|medium|hard|hardest"
}

function print_current()
{
    current=$(get_mame $DATA_VAR $DATA_FILE)
    case $current in
        default|easiest|easy|medium|hard|hardest)
            echo "$current"
            ;;
        "")
            _install_value
            echo "$DEFAULT_VALUE"
            ;;
        *)
            echo "unknown value"
            ;;
    esac
}

function _install_value()
{
    echo -e "\n$DATA_VAR         $DEFAULT_VALUE\n" >> $DATA_FILE
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

