#!/bin/bash

# escribid los scripts para que los tabuladores los convierta en 4 espacios.

# inicializaciones de paths, imprescindibles
# las variables de entorno son generadas por rgbux-env
. /opt/RGBux/bin/system-base

# contiene funciones de ayuda, como los replace
. /opt/RGBux/bin/rgbux-helpers


# ACCIONES

function do_BOOST()
{
    setgov performance
    echo "OK, new CPU-FREQ: PERFORMANCE"
}

function do_AUTO()
{
    setgov ondemand
    echo "OK, new CPU-FREQ: AUTO"
}


# HELPERS

function setgov()
{
    echo "$1" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
}


# FUNCIONES BASE

function runcmd()
{
    
    case $1 in
        "performance")
            # set value for autostart use
            replace_value "GOVERNOR" $1 $CFG_SYSTEM
            do_BOOST
            ;;
        "auto")
            # set value for autostart use
            replace_value "GOVERNOR" $1 $CFG_SYSTEM
            do_AUTO
            ;;
        *)
            echo "unknown option"
        ;;
    esac
}


function print_opts()
{
    echo "auto|performance"
}

function print_current()
{
    CURRENT=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor)
    if [ "$CURRENT" != "performance" ]; then
        echo "auto"
    else
        echo $CURRENT
    fi
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

