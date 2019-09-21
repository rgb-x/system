#!/bin/bash

################################################################################
#                                                                              #
################################################################################

# coge variables CORE, CFGS y PATHs
. /opt/RGBux/bin/launcher-ra-init

# Genera la variable SAVE_CFG para RETROARCH
. /opt/RGBux/bin/launcher-ra-saves

# preparamos la salida por si algo va mal, se recupere correctamente
trap 'restore_video; exit 0' EXIT

#Cargamos la rom añadiendo la configuración dinamica
CMD="retroarch -v -s \"$PARAM_SAVE\" -S \"$PARAM_SAVE\" $PARAM_CONFIG -L $2 \"$3\""
print_log "$CMD"
LANG=C retroarch -v -s "$PARAM_SAVE" -S "$PARAM_SAVE" $PARAM_CONFIG -L $2 "$3" 2>> /tmp/launcher.log


