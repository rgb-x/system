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

# DATA BASE
DATA_FILE=$CFG_SYSTEM
DATA_VAR="NEOGEO_BIOS"
DEFAULT_VALUE="euro"

# FUNCIONES BASE

function runcmd()
{
    
    case $1 in
        euro|us|japan|unibios23|unibios33)
            # set value for autostart use
            replace_value "$DATA_VAR" $1 $DATA_FILE
            echo "New Value: ${DATA_VAR} $1}!"
            ;;
        *)
            echo "unknown value"
            ;;
    esac
}


function print_opts()
{
    echo "euro|us|japan|unibios23|unibios33"
}

function print_current()
{
    current=""

    # compruebo que existe la variable en el entorno
    # por que por defecto no esta en RGBux
    if [[ -v NEOGEO_BIOS ]]; then
        current=$NEOGEO_BIOS
    else
        _install_value
        current=$DEFAULT_VALUE
    fi

    case $current in
        euro|us|japan|unibios23|unibios33)
            echo "$current"
            ;;
        *)
            echo "unknown value"
            ;;
    esac

}

function _install_value()
{
    add_value "${DATA_VAR}=${DEFAULT_VALUE}" $DATA_FILE
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

