#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
screen_lib.py.

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

import os, logging, subprocess
from math import ceil, floor

from .core_paths import ROOT_PATH
from .file_helpers import ini_get, ini_getlist

CFG_COMPMODES_FILE = os.path.join(ROOT_PATH, "ScreenUtilityFiles/modes.cfg")
DEFAULT_SCREEN_BIN = os.path.join(ROOT_PATH, "Datas/default.sh")

DEFAULT_RES = ["1920", "224", "60.000000", "-4", "-27", "3", "48", "192", "240", "5", "15734", "screen_lib", "H"]


class CRT(object):
    """CRT handler"""

    p_sTimingPath = ""

    m_dData = { "H_Res": 0,     # H_Res   - Horizontal resolution (1600 to 1920)
                "H_FP": 0,      # H_FP    - Horizontal Front Porch. Set to 48 if you don't know what you do
                "H_Sync": 0,    # H_Sync  - Horizontal Sync. Set to 192 if you don't know what you do
                "H_BP": 0,      # H_BP    - Horizontal Back Porch. Set to 240 if you don't know what you do
                "V_Res": 0,     # V_Res   - (50Hz : 192 to 288) - (60Hz : 192 a 256)
                "V_FP": 0,      # V_FP    - Vertical Front Porch
                "V_Sync": 0,    # V_Sync  - Vertical Sync. (3 to 10 or more...)
                "V_BP": 0,      # V_BP    - Vertical Back Porch
                "R_Rate": 0.0,  # R_Rate  - (47 a 62) MUST BE floating point
                "P_Clock": 0,   # P_Clock - Pixel_Clock
                # ------------------------------------- unknown values
                "H_Unk": 0, "V_Unk": 0,
                "Unk_0": 0, "Unk_1": 0, "Unk_2": 0,
                "Unk_R": 0, "Unk_P": 0,
                # ------------------------------------- use for calcs
                "H_Pos": 0,     # H_Pos   - Horizontal position of the screen (-10 to 10)
                "H_Zoom": 0,    # H_Zoom  - Horizontal size of the screen (-40 to 10)
                "V_Pos": 0,     # V_Pos   - Vertical position of the screen (-10 to 10)
                "H_Freq": 0,    # H_Freq  - Horizontal frequency of the screen. (15500 to 16000)
                # -------------------------------------

                # WARNING, all these values are intrinsically linked. If your screen is desynchronized, quickly reboot the RPI.
                # Some values will be limited due to other values.
    }

    m_iRSys = 0         # R_Sys   - Frontend rotation
    m_iRGame = 0        # R_Game  - Game rotation
    m_sSide_Game = ""   #

    def __init__(self, p_sSystem = "system"):
        self.m_sSystem = p_sSystem

    @staticmethod
    def get_xy_screen():
        return (320, 240)
        process = subprocess.Popen("/usr/bin/xrandr -q", stdout=subprocess.PIPE)
        output = process.stdout.read() # use commands?
        for line in output.splitlines():
            if 'x' in line and 'mode' in line:
                ResMode = line
                ResMode = ResMode.replace('"','').replace('x',' ').split(' ')
                x_screen = int(ResMode[1])
                y_screen = int(ResMode[2])
                return (x_screen, y_screen)

    def screen_restore(self):
        lValues = ini_getlist('/boot/config.txt', 'hdmi_timings')
        self.timing_reset()
        self.timing_parse_raw(lValues)
        self.resolution_call(**self.m_dData)

    def resolution_set(self):
        self.resolution_call(**self.m_dData)

    # FIXME: use internal data?
    def resolution_call(self, H_Res, H_FP, H_Sync, H_BP, H_Unk,
                             V_Res, V_FP, V_Sync, V_BP, V_Unk,
                             Unk_0, Unk_1, Unk_2,
                             R_Rate, Unk_R, P_Clock, Unk_P,
                             **_unused):
        # Generate vcgencmd command line in a string.
        cmd = "vcgencmd hdmi_timings "
        cmd += "%s %s %s %s %s " % ( H_Res, H_Unk, H_FP, H_Sync, H_BP )
        cmd += "%s %s %s %s %s " % ( V_Res, V_Unk, V_FP, V_Sync, V_BP )
        cmd += "%s %s %s " % ( Unk_0, Unk_1, Unk_2 )
        cmd += "%s %s %s %s > /dev/null" % ( R_Rate, Unk_R, P_Clock, Unk_P )
        self._command_call(cmd)

    def _command_call(self, p_sCMD):
        logging.info("CMD: %s" % p_sCMD)
        os.system(p_sCMD)



def selector_encapsulate(self):
    return 0
