#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_01."""

BASE = raw_input('Which base color, "Seattle Gray" or "Manatee"?: ')

if BASE == "Seattle Gray":
    ACCENT = raw_input('Which accent color, "Ceramic Glaze"' +
                       ' or "Cumulus Nimbus"?: ')
    if ACCENT == "Ceramic Glaze":
        HIGHLIGHT = raw_input('Which highlight color, "Basically White"' +
                              ' or "White"?: ')
    elif ACCENT == "Cumulus Nimbus":
        HIGHLIGHT = raw_input('Which highlight color, ' +
                              '"Off-White" or "Paper White"?: ')
    else:
        HIGHLIGHT = 'ERROR'
elif BASE == "Manatee":
    ACCENT = raw_input('Which accent color, ' +
                       '"Platinum Mist" or "Spartan Sage"?: ')
    if ACCENT == "Platinum Mist":
        HIGHLIGHT = raw_input('Which highlight color, ' +
                              '"Bone White" or "Just White"?: ')
    elif ACCENT == "Spartan Sage":
        HIGHLIGHT = raw_input('Which highlight color, ' +
                              '"Fractal White" or "Not White"?: ')
    else:
        HIGHLIGHT = 'ERROR'
else:
    ACCENT = 'ERROR'
    HIGHLIGHT = 'ERROR'

if HIGHLIGHT != 'ERROR':
    OUTPUT = ('Your selected colors are, {}, {}, and {}.'.format
              (BASE, ACCENT, HIGHLIGHT))
    print OUTPUT
else:
    print 'INPUT ERROR!'
