#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
configure wifi.py.

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
import sys
import os, logging, subprocess

sys.path.append('/opt/RGBux/bin/python')

from core.core_paths import BIN_PATH
from core.core_choices_dynamic import choices, pygame

WIFICMD = os.path.join(BIN_PATH, "wifi-cmd")

def show_passwd(p_sPasswd = " ****"):
    ch.set_title("PASSWORD %s" % ssid)
    ch.reset_data()
    ch.load_choices({p_sPasswd: -1})
    ch.show()

ch = choices()
ch.set_title("   CONFIGURE WIFI   ")

process = subprocess.Popen("sudo %s list" % WIFICMD, shell=True, stdout=subprocess.PIPE)
output = process.stdout.read() # use commands?

OPTIONS = {}
n = 0
for w in output.split("\n"):
    w = w.split(" ")
    n += 1
    try:
        wlabel = "%s (%s dB)" % ( w[2][:10], w[0] )
        OPTIONS[wlabel] = w[2]
    except:
        pass

    if n > 8: # max N rows
        break

ch.load_choices(OPTIONS)
ssid = ch.run()[0]

# now get password using choice lib
show_passwd()
writing=True
passwd=""
while writing:
    shift_pressed=False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                writing=False
                continue
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(1)
            elif event.key == pygame.K_SPACE:
                continue
            elif event.key == pygame.K_BACKSPACE:
                passwd=passwd[:-1]
            else:
                passwd+=event.unicode
            show_passwd(passwd)
            
ch.set_title("   CONFIGURE WIFI   ")
ch.reset_data()
ch.load_choices({"Conecting, please wait...": -1})
ch.show()

cmd = "sudo %s config enable %s %s" % (WIFICMD, ssid, passwd)
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
output = process.stdout.read() # use commands?
print output

if len(output) < 8:
    ch.reset_data()
    ch.load_choices({"Waiting ip...": -1})
    ch.show()
    pygame.time.delay(2000)
    cmd = "sudo %s ip" % WIFICMD
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output = process.stdout.read() # use commands?
    print output
    
ch.reset_data()
ch.load_choices({output.strip(): -1, "Press any key to exit.": -1})
ch.show()

if "error" in output:
    pygame.time.delay(2000)
    process = subprocess.Popen("sudo %s config disable" % WIFICMD, shell=True, stdout=subprocess.PIPE)
    process.wait()
    ch.cleanup()
    exit(1)
else:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                ch.cleanup()
                exit(0)
