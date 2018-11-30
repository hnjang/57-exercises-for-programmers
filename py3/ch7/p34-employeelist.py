#!/bin/usr/python

import sys
import random


def get_int(string=None):
    return int(input(string))


def print_employee(e):
    print('There are %d employees:' % len(e))
    for ee in e:
        print(ee)

employees = [
        'John Smith',
        'Jackie Jackson',
        'Chris Jones',
        'Amanda Cullen',
        'Jeremy Goodwin'
        ]

print_employee(employees)
name = input('Enter an employee name to remove: ')
if name in employees:
    employees.remove(name)
else:
    print('Not fount: %s' % name)
print_employee(employees)
