#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
configure updater.py 0.1

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
import os, logging, subprocess

sys.path.append('/home/david/almacen/nuevo/Desarrollo/Customs/rgbx/python')

from core.core_paths import CFG_PATH
from core.core_choices_dynamic import choices, pygame
from core.file_helpers import ini_get, ini_set

UPDATER_CFG = os.path.join(CFG_PATH, "updater-data.conf")

CH = choices()

def show_info(p_sInfo, p_sTitle = "RGBux Update"):
    CH.set_title(" %s" % p_sTitle)
    CH.reset_data()
    CH.load_choices({p_sInfo: -1})
    CH.show(False)


version=ini_get(UPDATER_CFG, "updater_ver")
root_url=ini_get(UPDATER_CFG, "updater_url")

# add version file to 
url = root_url + "version"
show_info("GET: ...%s" % url[32:], "RGBux Update SYS (%s)" % version)

try:
    contents = urllib2.urlopen(url).read().strip()
    print contents
    pygame.time.delay(1000)
except:
    show_info("Cannot connect or Wrong URL" % contents)
    pygame.time.delay(2000)
    exit(0)

if contents == version:
    show_info("Nothing to do, current (%s)" % contents)
    pygame.time.delay(2000)
    exit(0)

version=contents
url = root_url + "updater.py"

try:
    contents = urllib2.urlopen(url).read()
    print "updater downloaded", len(contents)
except:
    show_info("Cannot connect or Wrong URL" % contents)
    pygame.time.delay(2000)
    exit(0)

with open(__file__,"w") as f:
    f.write(contents)

if not ini_set(UPDATER_CFG, updater_ver, version):
    show_info("error writing version (%s)" % version)
    pygame.time.delay(2000)
    exit(0)
 
show_info("Process finished updated to: %s" % version)
pygame.time.delay(2000)
CH.cleanup()
exit(0)


