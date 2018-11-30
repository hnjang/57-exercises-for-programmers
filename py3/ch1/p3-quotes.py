#!/bin/usr/python

import sys


def readline():
    return sys.stdin.readline()


def get_int():
    return int(readline())

string = 'These aren\'t the droids you\'re looking for.'
print('%s\nWho said it? ' % string, end='')
sys.stdout.flush()
inp = readline().strip()
print('%s says, \"%s\"' % (inp, string))
