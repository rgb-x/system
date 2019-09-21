#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
launcher autocfg.py.

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

CMD_INFO = "info"
CMD_SELECTED = "current"

from core.core_choices_dynamic import choices, pygame

def run_cmd(p_sCmd):
    # log cmd
    logging.info(p_sCmd)
    process = subprocess.Popen(p_sCmd, shell=True, stdout=subprocess.PIPE)
    return process.stdout.read().strip() # use commands?

def show_info(p_sInfo):
    logging.info(p_sInfo)
    ch.reset_data()
    ch.load_choices({p_sInfo: -1})
    ch.show()
    pygame.time.delay(500)


BASEPATH = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.splitext(os.path.basename(__file__))[0]
MODSPATH = os.path.join(BASEPATH, FILENAME)
MODULES = [f for f in os.listdir(MODSPATH) if os.path.isfile(os.path.join(MODSPATH, f))]

OPTIONS={}
CURRENT=[]
BINARIES={}
NOPT=1

# GET MODULES AVAILABLE
for mod in MODULES:
    sTitle = "%i) %s" % (NOPT, os.path.splitext(mod)[0].upper())
    print "\t", sTitle
    modscript = os.path.join(MODSPATH, mod)

    # GET CURRENT VALUE
    sCurrentValue = run_cmd("%s %s" % (modscript, CMD_SELECTED))
    # GET OPTS
    output = run_cmd("%s %s" % (modscript, CMD_INFO))

    if len(output):
        lValues = output.split("|")
        iCnt = 0
        oDict = {}
        iCurrent = None
        for v in lValues:
            if sCurrentValue == v:
                iCurrent = (NOPT*10) + iCnt
            oDict[v] = (NOPT*10) + iCnt
            iCnt += 1
        if not iCurrent:
            print "Error in default value (%s), check current values in script (%s)." % (sCurrentValue, str(lValues))
            continue
        CURRENT.append(iCurrent)
        OPTIONS[sTitle] = oDict
        BINARIES[sTitle] = modscript
        NOPT += 1
        
     
print OPTIONS, CURRENT
logging.info("OPTS: %s %s" % (str(OPTIONS), str(CURRENT)))

OPTIONS["SAVE and EXIT"] = -1
ch = choices()
ch.set_title("   %s RGBUX   " % FILENAME.upper())
ch.load_choices(OPTIONS, list(CURRENT))
result = set(ch.run())

changed = result - set(CURRENT)

for o in changed:
    for opt, values in OPTIONS.iteritems():
        if type(values) == dict:
            for k, v in values.iteritems():
                if v == o:
                    cmd = "%s run %s" % (BINARIES[opt], k)
                    output = run_cmd(cmd)
                    show_info(output)

logging.info("RESULT: %s %s %s" % (str(changed), str(result), str(CURRENT)))
pygame.time.delay(2000)
ch.cleanup()
