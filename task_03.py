#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_03."""


import decimal

NAME = raw_input('What is your name? ')
PRINCIPAL = int(raw_input('What is the principal of the loan? '))
YEARS = int(raw_input('For how long is this being borrowed? '))
PREQUALIFIED = raw_input('Are you pre-qualified? ')
PREQUALIFIED = PREQUALIFIED.lower()
PREQUALIFIED = PREQUALIFIED[:1]
N = 12
INTEREST_RATE = 0
TOTAL = 0

if PRINCIPAL > 0 and PRINCIPAL <= 199999:
    if YEARS >= 1 and YEARS <= 15:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 3.63
        elif PREQUALIFIED == 'n':
            INTEREST_RATE = 4.65
    elif YEARS >= 16 and YEARS <= 20:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 4.04
        elif PREQUALIFIED == 'n':
            INTEREST_RATE = 4.98
    elif YEARS >= 21 and YEARS <= 30:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 5.77
        elif PREQUALIFIED == 'n':
            INTEREST_RATE = 6.39
elif PRINCIPAL >= 200000 and PRINCIPAL <= 999999:
    if YEARS >= 1 and YEARS <= 15:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 3.02
        elif PREQUALIFIED == 'n':
            INTEREST_RATE = 3.98
    elif YEARS >= 16 and YEARS <= 20:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 3.27
        elif PREQUALIFIED == 'n':
            INTEREST_RATE = 4.08
    elif YEARS >= 21 and YEARS <= 30:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 4.66
elif PRINCIPAL >= 1000000:
    if YEARS >= 1 and YEARS <= 15:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 2.05
    elif YEARS >= 16 and YEARS <= 20:
        if PREQUALIFIED == 'y':
            INTEREST_RATE = 2.62

if PREQUALIFIED == 'y':
    PREQUALIFIED = 'Yes'
elif PREQUALIFIED == 'n':
    PREQUALIFIED = 'No'

if INTEREST_RATE:
    INTEREST_RATE = decimal.Decimal(INTEREST_RATE/100)
    TOTAL = PRINCIPAL * ((1 + (INTEREST_RATE/N)) ** (N * YEARS))
    TOTAL = round(TOTAL)

LINE = '-' * 80 + '\n'
YEARSTR = str(YEARS) + 'yrs'
PRINCIPALSTR = '${:,.0f}'.format(PRINCIPAL)

if TOTAL:
    TOTALSTR = '${:,.0f}'.format(TOTAL)
else:
    TOTALSTR = 'None'

REPORT = ('Loan Report for: {} \n' + LINE +
          '\t Principal:\t {:>10} \n' +
          '\t Duration:\t {:>10} \n' +
          '\t Pre-qualified?: {:>10} \n' +
          ' \n' +
          '\t Total:\t\t {:>10}')

print REPORT.format(NAME, PRINCIPALSTR, YEARSTR, PREQUALIFIED, TOTALSTR)
