#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
paths_lib.py.

https://github.com/krahsdevil/crt-for-retropie/

Copyright (C)  2018/2019 -krahs- - https://github.com/krahsdevil/
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

import os, logging

TMP_RGBUX_PATH = "/tmp"

# retropie path setup
ROOT_PATH = "/opt"

SYS_PATH = os.path.join(ROOT_PATH, "RGBux")
BIN_PATH = os.path.join(SYS_PATH, "bin")
CFG_PATH = os.path.join(SYS_PATH, "configs")

RA_PATH  = os.path.join(ROOT_PATH, "retroarch")

LOG_PATH = os.path.join(TMP_RGBUX_PATH, "python_scripts.log")
__DEBUG__ = logging.INFO # logging.ERROR

logging.basicConfig(filename=LOG_PATH, level=__DEBUG__, format='[%(asctime)s] %(levelname)s - %(filename)s:%(funcName)s - %(message)s')

