#!/bin/bash

################################################################################
#                                                                              #
################################################################################

# Config video no necesaria se encarga 15khz-switchres-exec

# Genera la variable CORE y los CFGs
. /opt/RGBux/bin/launcher-ra-init


exec /opt/RGBux/bin/15khz-switchres-exec 640 480 60 retroarch --config $CONFIG_FILE "$@"
