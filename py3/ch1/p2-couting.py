#!/bin/usr/python

import sys


def readline():
    return sys.stdin.readline()


def get_int():
    return int(readline())

print('What is the input string? ', end='')
sys.stdout.flush()
inp = readline().strip()
print('%s has %d characters.' % (inp, len(inp)))
