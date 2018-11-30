#!/bin/usr/python

import sys
from datetime import datetime


def readline():
    return sys.stdin.readline()


def get_int(string=None):
    if string is not None:
        print(string, end='')
        sys.stdout.flush()
    return int(readline())

age = get_int('What is your current age? ')
retire_age = get_int('At what age would you like to retire? ')
remain = retire_age - age
if remain < 0:
    print('remain is %d. something wrong!' % remain)
    sys.exit(-1)

current_year = datetime.today().year
remain_year = current_year + remain
print('It\'s %d, so you can retire in %d.' % (current_year, remain_year))
