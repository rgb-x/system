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

sys.path.append('/opt/RGBux/bin/python')

from core.file_helpers import ini_get, ini_set

def run_cmd(p_sCmd):
    # log cmd
    logging.info(p_sCmd)
    process = subprocess.Popen(p_sCmd, shell=True, executable="/bin/bash")
    process.wait()

run_cmd("/opt/RGBux/frontend/launchers/lanzadorRA.sh")

exit(0)


