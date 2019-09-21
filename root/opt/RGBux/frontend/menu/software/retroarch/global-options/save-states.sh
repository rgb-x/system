#!/bin/bash

function runcmd()
{
    echo "SORRY ALLWAYS DISABLED - WIP ($1)"
}

function print_opts()
{
    echo "OFF|ON"
}

function print_current()
{
    echo "OFF"
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

