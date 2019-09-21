#!/bin/bash

################################################################################
# GROOVYMAME LAUNCHER
################################################################################

# coge variables CORE, CFGS y PATHs
. /opt/RGBux/bin/launcher-mame-init

# PARAM_DEBUG="-verbose"
# PARAM_LOG="&> /tmp/mame.log"

# preparamos la salida por si algo va mal, se recupere correctamente
trap 'recover_gm; exit 0' EXIT

/opt/groovymame/mame64 -nokeepaspect $PARAM_DEBUG $PARAM_NEOGEO "$@" $PARAM_LOG

