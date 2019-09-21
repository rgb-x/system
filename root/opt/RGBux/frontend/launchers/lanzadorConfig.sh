#!/bin/bash

################################################################################
# Config pyGAME Launcher
################################################################################

# falla en algunas tarjetas nuevas. deshabilitado por el momento
#exec /opt/RGBux/bin/15khz-switchres-exec 320 240 60 "$@"

"$@" 2> /tmp/launcher.cfg.log


exit 0