#!/bin/bash

URL="https://github.com/rgb-x/RGB-UX/releases/download/upt.02/update-02.1.tar.bz2"
PACKAGE=/tmp/wine.tar.bz2

wget "$URL" -O $PACKAGE
cd /home/arcade && tar xjf $PACKAGE
sudo apt-get update
sudo apt-get install --install-recommends -y winehq-stable
