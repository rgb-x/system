#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
configure wifi.py.

custom library for RGBux
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
import sys, time, random
import os, logging, subprocess

sys.path.append('/opt/RGBux/bin/python')

from core.core_choices_dynamic import choices, pygame
from core.file_helpers import touch_file

TMP_FLAGFILE = "/tmp/xfinder-found"
MAX_TIME = 9

if len(sys.argv) != 2:
    exit(2)

def show_data(p_sTime, p_sString = ""):
    ch.set_title("XORG CHECK PORT: %s (%s)" % (PORT, p_sTime))
    if not p_sString:
        p_sString = "..."
    sstr = "write %s : %s" % (PHRASE, p_sString)
    ch.reset_data()
    ch.load_choices({sstr: -1,})
    ch.show()

OPTIONS = {}
PORT = sys.argv[1]
PHRASE = str(random.randint(100,999))
VIDEO_OK = False
ch = choices()

ch.set_title("XORG CHECK PORT: %s" % PORT)
ch.load_choices({"Do you see me?": -1,})
ch.show(False)
pygame.time.delay(1000)


# now get sentence using choice lib
writing=True
sentence=""
start_time = time.time()
while writing:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            start_time = time.time()
            if event.key == pygame.K_RETURN:
                writing = False
                continue
            elif event.key == pygame.K_SPACE:
                continue
            elif event.key == pygame.K_BACKSPACE:
                sentence=sentence[:-1]
            else:
                sentence+=event.unicode
    current_time = int(time.time() - start_time)
    if current_time > MAX_TIME:
        writing = False
    show_data(str(current_time), sentence)
            

if sentence != PHRASE:
    ch.cleanup()
    exit(1)

print "OK!"
ch.reset_data()
ch.set_title("   CONFIGURE XORG   ")
ch.load_choices({"OK! Saving data. Please wait...": -1})
ch.show()

touch_file(TMP_FLAGFILE)
pygame.time.delay(2000)

ch.cleanup()
exit(0)

