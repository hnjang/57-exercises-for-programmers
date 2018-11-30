#!/bin/usr/python

import sys


def readline():
    return sys.stdin.readline()


def get_int():
    return int(readline())

query = ['a noun', 'a verb', 'an adjective', 'an adverb']
inp = {}

for q in query:
    print('Enter %s: ' % q, end='')
    sys.stdout.flush()
    inp[q] = readline().strip()

print(
        'Do you %s your %s %s %s? That\'s hilarious!' %
        (inp['a verb'], inp['an adjective'], inp['a noun'], inp['an adverb']))
