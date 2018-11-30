#!/bin/usr/python

import sys


def readline():
    return sys.stdin.readline()


def get_int():
    return int(readline())

print('What is your name? ', end='')
sys.stdout.flush()
name = readline().strip()
print('Hello, %s, nice to meet you!' % name)
