#!/bin/bash

################################################################################
################################################################################

exec /opt/RGBux/bin/15khz-switchres-exec 640 480 60 /usr/games/PCSX2-linux.sh --nogui --fullscreen "$@"

exit 0
