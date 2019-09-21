#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
launcher core.py.

launcher library for retropie, based on original idea - Ironic
  and the retropie integration work by -krahs-

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

"""
### HOW TO THEME YOUR CHOICES!!

    # first get default cfg
    custom_cfg = DEFAULT_CFG

    # change some default values (see DEFAULT_CFG to see options)
    custom_cfg['font'] = "font_16.ttf"
    custom_cfg['font_size'] = 16
    custom_cfg['bgcolor'] = (80, 180, 120)

    # init class using your theme
    ch = choices(custom_cfg)

"""


import os, sys
import logging
import pygame

from .core_paths import SYS_PATH
#from .screen import CRT
from .core_controls import joystick, CRT_UP, CRT_DOWN, CRT_BUTTON, CRT_OK, CRT_CANCEL

SKINSELECTOR_PATH = os.path.join(SYS_PATH, "data", "selector_themes")

# BASE COLORS
BG_COLOR = (128, 120, 211)
BG_COLOR_SEL = (180, 80, 100)

# BG TYPES
BG_FLAT = 1
BG_DEGRADE = 2
SCREEN_SIZE = (320, 240)
#SCREEN_FLAGS = pygame.OPENGL | pygame.FULLSCREEN | pygame.DOUBLEBUF
SCREEN_FLAGS = pygame.NOFRAME | pygame.HWSURFACE | pygame.DOUBLEBUF
#SCREEN_FLAGS = pygame.NOFRAME

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
os.environ['SDL_DEBUG'] = "1"


DEFAULT_CFG = {
    'style': "choice_dynamic",

    'border': "border.png",
    'border_corner': "border_corner.png",
    'border_height': 8,

    'cursor': "cursor.png",
    'font': "font.ttf",
    'font_size': 16,
    'snd_cursor': "cursor.wav",
    'snd_load': "load.wav",

    'bgcolor': BG_COLOR,
    'bgcolor_selected': BG_COLOR_SEL,
    'bgtype': BG_DEGRADE,
}

# internal
C_BLACK = pygame.Color(  0,   0,   0)
C_WHITE = pygame.Color(255, 255, 255)
FPS = 60

class choices(object):
    """show a selector with choices using pygame."""

    m_oJoyHandler = None
    m_oClock = None
    m_lOpts = []
    m_dMainMenu = {}
    m_lValues = []
    m_bSimpleMode = False
    m_iCurrent = 0
    m_sSkinPath = ""
    m_SndCursor = None
    m_SndLoad = None
    m_lResolutionXY = ()
    m_bOnlyJoy = False
    m_bIsChild = False # sub option
    m_oScreen = None
    m_bUpdateScreen = True
    m_oFont = None
    m_oTitle = None
    m_oTable = None
    m_oCursor = None
    m_bShowCursor = True

    def __init__(self, p_dChoices = DEFAULT_CFG):
        self.dCFG = p_dChoices
        self.m_sSkinPath = os.path.join(SKINSELECTOR_PATH, self.dCFG['style'])
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        self.m_oClock = pygame.time.Clock()
        self.oJoyHandler = joystick()
        self._init_screen()
        self._init_sounds()

    def _init_screen(self):
        pygame.display.init()
        pygame.font.init()
        pygame.mouse.set_visible(0)

        # gfx
        self.m_oFontText = pygame.font.Font(os.path.join(self.m_sSkinPath,
            self.dCFG['font']),
            self.dCFG['font_size'])
        self.dCFG['font_line'] = self.m_oFontText.get_linesize()

        self.be = pygame.image.load(os.path.join(self.m_sSkinPath, self.dCFG['border_corner']))
        self.b = pygame.image.load(os.path.join(self.m_sSkinPath, self.dCFG['border']))

        # screen
        self.m_oScreen = pygame.display.set_mode((0,0), SCREEN_FLAGS)
        self.m_lResolutionXY = self.m_oScreen.get_size()
        self.m_lScreenCenter = map(lambda x: x/2, self.m_lResolutionXY)

    def _init_sounds(self):
        try:
            self.m_SndCursor = pygame.mixer.Sound(os.path.join(self.m_sSkinPath, self.dCFG['snd_cursor']))
            self.m_SndLoad = pygame.mixer.Sound(os.path.join(self.m_sSkinPath, self.dCFG['snd_load']))
        except Exception as e:
            logging.error(e)

    def _add_opt(self, p_lOptPath):
        try:
            dData = {}
            dData['text'], dData['value'] = p_lOptPath
            if type(dData['value']) == dict:
                for k,v in dData['value'].iteritems():
                    if v in self.m_lValues:
                        dData['text'] = "%s    <%s>" % (dData['text'], str(k))
            
            dData['img'] = self.text_render(dData['text'], C_WHITE, C_BLACK)
            self.m_lOpts.append(dData)
        except Exception as e:
            logging.error(str(e))

    def _set_value(self, p_iValue):
        if self.m_bSimpleMode:
            self.m_lValues = [p_iValue]
            return
        p = int(p_iValue/10) # values 1x, 2x, 3x, ...
        print p - 1, "=" , p_iValue
        self.m_lValues[p - 1] = p_iValue

    def set_title(self, p_sTitle, p_lColor = C_WHITE, p_lShadowColor = C_BLACK):
        self.m_oTitle = self.text_render(p_sTitle, p_lColor, p_lShadowColor)
        self.m_iTitleSize = self.dCFG['font_line'] + (self.dCFG['border_height'] * 2) + 1

    def reset_data(self):
        self.m_lOpts = []

    def _choices_create(self, p_dOpts):
        for opt in sorted(p_dOpts.iteritems()):
            self._add_opt(opt)
        self._table_render()
    
    def load_selections(self, p_lValues):
        if p_lValues == None:
            self.m_lValues = []
            self.m_bSimpleMode = True
        self.m_lValues = p_lValues
        
    def load_choices(self, p_dOpts, p_lValues = None):
        self.m_dMainMenu = p_dOpts
        self.load_selections(p_lValues)
        self._choices_create(p_dOpts)

    def _table_create(self):
        self.m_oTable = Table(0, self.dCFG['font_line'] * len(self.m_lOpts))
        if self.m_oTitle and not self.m_bIsChild:
            self.m_oTable.width = self.m_oTitle.get_width()
            self.m_oTable.height += self.m_iTitleSize
        for opt in self.m_lOpts:
            if opt['img'].get_width() > self.m_oTable.width:
                self.m_oTable.width = opt['img'].get_width()
        self.m_oTable.width += self.dCFG['border_height'] * 4
        self.m_oTable.height += self.dCFG['border_height'] * 2
        self.m_oTable.img = pygame.Surface(self.m_oTable.get_size())
        rect = self.m_oTable.img.get_rect()
        rect.center = self.m_lScreenCenter
        self.m_oTable.position = rect
        self.m_oTable.fill(self.dCFG['bgcolor'], self.dCFG['bgtype'])
        

    def _cursor_reset(self):
        self._cursor_create()
        
    def _cursor_create(self):
        self.m_oCursor = Cursor(self.m_oTable.position.x, self.m_oTable.position.y)
        self.m_oCursor.img = pygame.image.load(os.path.join(self.m_sSkinPath, self.dCFG['cursor']))
        y = self.m_oTable.position.y + self.dCFG['border_height']
        if self.m_oTitle and not self.m_bIsChild:
            y += self.m_iTitleSize
        self.m_oCursor.set_top(y)


    def _table_border(self):
        top = 0
        # title
        if self.m_oTitle and not self.m_bIsChild:
            bottom = self.m_iTitleSize - self.be.get_height() - 1
            self._draw_border(top, bottom)
            top = bottom + self.be.get_height() + 1
        bottom = self.m_oTable.img.get_height() - self.be.get_height()
        self._draw_border(top, bottom)

    def _draw_border(self, top, bottom):
        w = self.be.get_width()
        h = self.be.get_height()
        right = self.m_oTable.img.get_width() - w

        # edges
        tmp = pygame.transform.flip(self.b, 0, 1)
        for x in range(w, right):
            self.m_oTable.img.blit(self.b, (x, top))
            self.m_oTable.img.blit(tmp, (x, bottom))
        tmp = pygame.transform.rotate(self.b, 90)
        tmp2 = pygame.transform.rotate(self.b, -90)
        for y in range(h + top, bottom):
            self.m_oTable.img.blit(tmp, (0, y))
            self.m_oTable.img.blit(tmp2, (right, y))

        # corners
        self.m_oTable.img.blit(self.be, (0, top))
        tmp = pygame.transform.rotate(self.be, -90)
        self.m_oTable.img.blit(tmp, (right, top))
        tmp = pygame.transform.rotate(self.be, 180)
        self.m_oTable.img.blit(tmp, (right, bottom))
        tmp = pygame.transform.rotate(self.be, 90)
        self.m_oTable.img.blit(tmp, (0, bottom))

    def _table_render(self):
        self._table_create()
        self._table_border()
        self._cursor_create()
        line = self.dCFG['border_height']

        # title
        if self.m_oTitle and not self.m_bIsChild:
            rect = self.m_oTitle.get_rect()
            #rect.center = self.m_lScreenCenter
            rect.x = (self.m_oTable.width - self.m_oTitle.get_width()) / 2
            rect.y = line
            self.m_oTable.img.blit(self.m_oTitle, rect)
            line += self.m_iTitleSize

        for opt in self.m_lOpts:
            rect = opt['img'].get_rect()
            rect.x = 16
            rect.top = line
            self.m_oTable.img.blit(opt['img'], rect)
            line += self.dCFG['font_line']

    def text_render(self, p_sText, p_lTextColor, p_lShadowColor = None, p_iShadowDrop = 1, p_bUseBiggerFont = True):
        img = self.m_oFontText.render(p_sText, False, p_lTextColor)
        rect = img.get_rect()
        sf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        if p_lShadowColor:
            shadow = self.m_oFontText.render(p_sText, False, p_lShadowColor)
            shadow_rect = img.get_rect()
            shadow_rect.x += p_iShadowDrop
            shadow_rect.y += p_iShadowDrop
            sf.blit(shadow, shadow_rect)
        sf.blit(img, rect)
        return sf

    def cleanup(self):
        pygame.display.quit()
        pygame.quit()

    def show(self, p_bShowCursor = True):
        self.m_bUpdateScreen = 2
        self.m_bShowCursor = p_bShowCursor
        self._update_screen()
        #pygame.time.delay(100)

    def run(self):
        if self.oJoyHandler.get_num() < 1:
            # TODO: no opts or no joys
            logging.error("no joysticks found.")
            if self.m_bOnlyJoy:
                logging.error("select default opt")
                return self._choice_select()
        self._update_screen()
        result = self.loop()
        return result

    def loop(self):
        while True:
            #self.m_oClock.tick(FPS)
            event = self.oJoyHandler.event_wait()
            #logging.info("event %s" % str(event))
            if event & CRT_UP:
                self.m_SndCursor.play()
                self._choice_change(-1)
            if event & CRT_DOWN:
                self.m_SndCursor.play()
                self._choice_change(1)
            if event & CRT_OK:
                self.m_SndLoad.play()
                if self._choice_select() == -1:
                    break
            if event & CRT_CANCEL:
                    exit(1)
                
            if self.m_bUpdateScreen:
                self._update_screen()
                
        logging.info("finished: %s" % str(self.m_lValues))
        return self.m_lValues


    def _choice_select(self):
        text = self.m_lOpts[self.m_oCursor.pointer]['text']
        selected = self.m_lOpts[self.m_oCursor.pointer]['value']
        print "selected %s" % text
        if type(selected) == dict:
            self.m_bIsChild = True
            self.dCFG['bgcolor'] = self.dCFG['bgcolor_selected']
            self.reset_data()
            self._choices_create(selected)
            self.m_oTable.position.y = self.m_oCursor.y
            self._cursor_reset()
            self.m_bUpdateScreen = 1
            return None
        elif self.m_bIsChild:
            self.m_oScreen.fill(C_BLACK)
            self.m_bIsChild = False
            self.dCFG['bgcolor'] = BG_COLOR
            self.reset_data()
            if selected != -1:
                self._set_value(selected)
            self._choices_create(self.m_dMainMenu)
            self._cursor_reset()
            self.m_bUpdateScreen = 1
        elif self.m_bSimpleMode:
            self._set_value(selected)
            selected = -1
        return selected
            
            

    # TODO: allow another directions, atm is a simple up to down cursor
    def _choice_change(self, p_iDirection):
        self.m_oCursor.pointer += p_iDirection
        if self.m_oCursor.pointer >= len(self.m_lOpts):
            self.m_oCursor.pointer = 0
        elif self.m_oCursor.pointer < 0:
            self.m_oCursor.pointer = len(self.m_lOpts) - 1
        self.m_oCursor.y = self.m_oCursor.top + (self.m_oCursor.pointer * self.dCFG['font_line'])
        self.m_bUpdateScreen = 1

    def _update_screen(self):
        self._draw_screen()
        self.m_bUpdateScreen = None

    def _draw_screen(self):
        if self.m_bUpdateScreen == 2:
            self.m_oScreen.fill(C_BLACK)
        self.m_oScreen.blit(self.m_oTable.img, self.m_oTable.position)
        if self.m_bShowCursor:
            self.m_oScreen.blit(self.m_oCursor.img, (self.m_oCursor.x, self.m_oCursor.y))
        pygame.display.flip()


class Cursor(object):
    img = None
    top = 0
    pointer = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def set_top(self, p_iTop):
        self.top = self.y = p_iTop

        
class Table(object):
    """docstring for Table."""
    img = None
    height = 0
    width = 0
    position = 0

    def __init__(self, w, h):
        self.height = h
        self.width = w

    def __str__(self):
        return str((self.width, self.height, self.position, self.img))

    def get_size(self):
        return (self.width, self.height)

    def fill(self, p_lBaseColor, p_iType):
        if p_iType == BG_FLAT:
            self.img.fill(p_lBaseColor)
            return
        ndeg = min(p_lBaseColor)/8
        height = (self.height/ndeg) + 1
        cont = 0
        for y in range(0, self.height, height):
            color = map(lambda x: x - (8 * cont), p_lBaseColor)
            pygame.draw.rect(self.img, color, (0,y, self.width, height) )
            cont += 1
