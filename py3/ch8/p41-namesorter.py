#!/bin/usr/python

import sys
import random


def get_int(string=None):
    return int(input(string))


def print_list(l, string=None):
    if string is not None:
        print(string)
    for ll in l:
        print(ll)


def get_list_from_file(fname):
    with open(fname) as f:
        res = f.read().strip().split('\n')
    return res


def put_list_to_file(fname, l):
    with open(fname, 'w') as f:
        f.write('\n'.join(l))

names = get_list_from_file('p41-in.txt')
names = sorted(names)
put_list_to_file('p41-out.txt', names)
string = ('Total of %d names\n' % len(names)) + '-' * 20
print_list(names, string)
