#!/bin/bash

URL="https://github.com/rgb-x/RGB-UX/releases/download/upt.02/wine-4.10-pr.tar.bz2"
PACKAGE=/tmp/wine.tar.bz2
INSDIR=/opt/RGBux/data/wine

wget "$URL" -O $PACKAGE
sudo mkdir -p $INSDIR

echo "decompress..."
cd $INSDIR && sudo tar xjf $PACKAGE

sudo apt-get update
sudo apt-get install --install-recommends -y wine-staging wine-staging-amd64 wine-staging-i386
