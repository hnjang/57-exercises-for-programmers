#!/bin/usr/python

import sys
import random


def get_int(string=None):
    return int(input(string))

answers = ['Yes', 'No', 'Maybe', 'Ask again later']

inp = input('What\'s your question? ')
random.seed()
rnd = random.randrange(4)
print(answers[rnd])
