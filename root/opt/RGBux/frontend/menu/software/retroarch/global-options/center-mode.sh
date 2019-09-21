#!/bin/bash

# escribid los scripts para que los tabuladores los convierta en 4 espacios.

# inicializaciones de paths, imprescindibles
# las variables de entorno son generadas por rgbux-env
. /opt/RGBux/bin/system-base

# contiene funciones de ayuda, como los replace
. /opt/RGBux/bin/rgbux-helpers


# INIT VARS
RGBUX_CFG=$RG_RA_CFG/ra-rgbux.cfg
RG_RA_CRT_NAME=crt_switch_resolution_super


function runcmd()
{
    local value
    case $1 in
        # necesito convertir estos dos por que estan con el nombre para humanos
        NATIVE)
            value=0
            ;;
        DYNAMIC)
            value=1
            ;;
        1920|2560|3840)
            value=$1
            ;;
        *)
            echo "value unknown!"
            ;;
    esac
    
    replace_value $RG_RA_CRT_NAME $value $RGBUX_CFG
    echo "DONE! now using $1"
}

function print_opts()
{
    echo "-4|-3|-2|-1|0|+1|+2|+3|+4"
}

function print_current()
{
    local current=$(get_value $RG_RA_CRT_NAME $RGBUX_CFG)
    
    case $current in
        # cambiamos los valores internos por algo entendible por humanos
        0)
            echo "NATIVE"
            ;;
        1)
            echo "DYNAMIC"
            ;;
        # estos no son necesarios, se entienden... espero
        1920|2560|3840)
            echo "$current"
            ;;
        *)
            echo "current value unknown!"
            ;;
    esac
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

