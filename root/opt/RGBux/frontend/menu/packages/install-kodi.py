#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
configure installer.py 0.1

launcher library for RGBux
    https://github.com/rgbx/

Copyright (C)  2019 dskywalk - http://david.dantoine.org

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 2 of the License, or (at your option) any
later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
import sys, urllib2
import os, logging, subprocess, requests, commands

sys.path.append('/opt/RGBux/bin/python')

from core.core_paths import CFG_PATH
from core.core_choices_dynamic import choices, pygame
from core.file_helpers import dw_file

UPDATER_TITLE = "RGBux - Install KODI (v1)"

CH = choices()

def show_info(p_sInfo, p_sTitle = UPDATER_TITLE):
    CH.set_title(" %s" % p_sTitle)
    CH.reset_data()
    CH.load_choices({p_sInfo: -1})
    CH.show(False)

def run_cmd(p_sCmd):
    # log cmd
    logging.info(p_sCmd)
    #process = subprocess.Popen(p_sCmd, shell=True, stdin=None, executable="/bin/bash")
    #process = subprocess.Popen(p_sCmd, shell=True, stdout=subprocess.PIPE)
    #process.wait() # use commands?
    print commands.getoutput(p_sCmd)

if os.environ['ISLIVE'] == "true":
    print "NOT LIVE"
    show_info("You cannot install in LIVE...")
    pygame.time.delay(2000)
    exit(1)

show_info("This script is a Work In Progress...")
pygame.time.delay(2000)
exit(1)

show_info("Install KODI packages. About 100Mb will be used, Please Wait...")
run_cmd("sudo apt-get -yq install --install-suggests kodi")


show_info("Clean cache...")
run_cmd("sudo apt-get clean")

show_info("Process finished!")
pygame.time.delay(2000)
CH.cleanup()
exit(0)

