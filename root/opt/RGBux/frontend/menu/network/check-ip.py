#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
configure check-ip.py.

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
import sys
import os, logging, subprocess

sys.path.append('/opt/RGBux/bin/python')

from core.core_choices_dynamic import choices, pygame

def run_cmd(p_sCmd):
    # log cmd
    logging.info(p_sCmd)
    process = subprocess.Popen(p_sCmd, shell=True, stdout=subprocess.PIPE)
    return process.stdout.read().strip() # use commands?

ch = choices()
ch.set_title("   CHECK IP   ")

output = run_cmd("ifconfig | grep broadcast")

OPTIONS = {}
n = 0
for w in output.split("\n"):
    w = w.strip().split(" ")
    print w
    try:
        wlabel = "  IP: %s " % ( w[1] )
        OPTIONS[wlabel] = -1
    except:
        pass


ch.load_choices(OPTIONS)
result = ch.run()

ch.set_title("   RESTART ETHERNET?   ")
ch.reset_data()
ch.load_choices({"Yes": 1, "No": 0})
result = ch.run()[0]

print result
if result:
    print "restart!!"
    ch.reset_data()
    ch.load_choices({"restarting network, please wait...": -1})
    ch.show(False)
    run_cmd("sudo systemctl restart networking.service")
    run_cmd("sudo systemctl restart smbd.service")
    run_cmd("sudo systemctl restart nmbd.service")
    ch.load_choices({"Done!": -1})
    ch.show(False)
    

pygame.time.delay(2000)
ch.cleanup()


