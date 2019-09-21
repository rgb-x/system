#!/bin/bash

# escribid los scripts para que los tabuladores los convierta en 4 espacios.

# inicializaciones de paths, imprescindibles
# las variables de entorno son generadas por rgbux-env
. /opt/RGBux/bin/system-base


# ACCIONES

function do_GAME()
{
    # "2>" significa que los errores no se muestren
    mv $BOOT_GAME_CFG.off $BOOT_GAME_CFG 2> /dev/null
    # esto sera lo que se muestre en pantalla
    echo "OK, edit $BOOT_GAME_CFG to change game"
}

function do_FE()
{
    # "&>" significa que no se muestre nada
    mv $BOOT_GAME_CFG $BOOT_GAME_CFG.off &> /dev/null
    # esto sera lo que se muestre en pantalla
    echo "OK, disabled!"
}


# FUNCIONES BASE

function runcmd()
{
    case $1 in
        "GAME")
            do_GAME
            ;;
        "FRONTEND")
            do_FE
            ;;
        *)
        echo "unknown option"
        ;;
    esac
}

function print_opts()
{
    echo "GAME|FRONTEND"
}

function print_current()
{
    if [ -e $BOOT_GAME_CFG ]; then
        echo "GAME"
    else
        echo "FRONTEND"
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

