#!/bin/usr/python

import sys


def readline():
    return sys.stdin.readline()


def get_int(string=None):
    if string is not None:
        print(string, end='')
        sys.stdout.flush()
    return int(readline())

f = get_int('What is the first number? ')
s = get_int('What is the second number? ')

print('%d + %d = %d' % (f, s, f+s))
print('%d - %d = %d' % (f, s, f-s))
print('%d * %d = %d' % (f, s, f*s))
print('%d / %d = %d' % (f, s, f/s))
