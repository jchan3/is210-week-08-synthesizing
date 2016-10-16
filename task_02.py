#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_02."""

DAY = raw_input('What Day is it? ').lower()
TIME = int(raw_input('What Time is it? (Enter a 4-digit number without ' +
                     'a colon)? '))
DAY = DAY[:3]
SNOOZE = True if ((DAY == 'sat' or DAY == 'sun') or
                  TIME < 600) else False

if SNOOZE is False:
    print 'Beep! ' * 5
