#!/bin/bash

################################################################################
#                                                                              #
################################################################################

# Config video no necesaria se encarga 15khz-switchres-exec

# Genera la variable CORE y los CFGs
. /opt/RGBux/bin/launcher-init


exec /opt/RGBux/bin/15khz-switchres-exec 768 272 50 retroarch --config $CONFIG_FILE "$@"

