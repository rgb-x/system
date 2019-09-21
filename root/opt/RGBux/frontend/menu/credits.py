#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
system creditos.py 0.1

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
import sys, urllib2, pygame
import os, logging, subprocess

sys.path.append('/opt/RGBux/bin/python')

from core.core_choices_dynamic import SKINSELECTOR_PATH, SCREEN_FLAGS, DEFAULT_CFG
from core.cr import cr_l as credit_list

m_sSkinPath = os.path.join(SKINSELECTOR_PATH, "choice_dynamic")
m_sMusicPath = os.path.join(SKINSELECTOR_PATH, "../", "cr-music.ogg")
m_oScreenSize = (0,0)
m_oScreen = None
m_oFontText = None
m_lScreenCenter = None
textsf = []

pygame.display.init()
pygame.font.init()
pygame.mouse.set_visible(0)
pygame.mixer.init()

# gfx
m_oFontText = pygame.font.Font(os.path.join(m_sSkinPath,
    DEFAULT_CFG['font']),
    DEFAULT_CFG['font_size']*2)
DEFAULT_CFG['font_line'] = m_oFontText.get_linesize()

# screen
m_oScreen = pygame.display.set_mode(m_oScreenSize, SCREEN_FLAGS)
m_oScreenRect = m_oScreen.get_rect()
m_lResolutionXY = m_oScreen.get_size()
m_lScreenCenter = map(lambda x: x/2, m_lResolutionXY)
    
clock = pygame.time.Clock()

for i, line in enumerate(credit_list):
    s = m_oFontText.render(line, 1, (250, 250, 250))
    r = s.get_rect(centerx=m_oScreenRect.centerx, y=m_oScreenRect.bottom + i * 90)
    textsf.append((r, s))

pygame.mixer.music.load(m_sMusicPath)
pygame.mixer.music.play()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN or e.type == pygame.JOYBUTTONDOWN:
            exit(0)

    m_oScreen.fill((0, 0, 0))

    for r, s in textsf:
        # now we just move each rect by one pixel each frame
        r.move_ip(0, -1)
        # and drawing is as simple as this
        m_oScreen.blit(s, r)

    # if all rects have left the screen, we exit
    if not m_oScreenRect.collidelistall([r for (r, _) in textsf]):
        break

    # only call this once so the screen does not flicker
    pygame.display.flip()

    # cap framerate at 60 FPS
    clock.tick(60)

exit(0)


