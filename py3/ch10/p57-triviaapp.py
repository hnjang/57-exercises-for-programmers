#!/bin/usr/python

import sys
import json
import random
from pprint import pprint


def get_valid_answer():
    string = "answer [a/b/c/d]: "
    while True:
        answer = input(string)
        if len(answer) != 1: continue
        if answer not in 'abcd': continue
        return answer


def play_game(l_qst, q_data):
    fmt = '\n{}\n[a] {}\n[b] {}\n[c] {}\n[d] {}'
    for c, idx in enumerate(l_qst):
        q = q_data['quiz'][idx]
        print(fmt.format(
            q['question'], q['ex1'], q['ex2'], q['ex3'], q['ex4']))
        answer = get_valid_answer()
        if answer != q['answer']:
            print('You miss. Correct answer is %s' % (q['answer']))
            print('Game over. You failed on %dth question' % (c+1))
            return False
    print('Congrat. You got all %d questions' % (c+1))
    return True


with open('p57-quiz.json') as f:
    q_data = json.load(f)
random.seed()
original_qst = list(range(int(q_data['count'])))
qst = []
for i in range(len(original_qst)):
    r = random.randrange(len(original_qst))
    qst.append(original_qst[r])
    original_qst.remove(original_qst[r])
play_game(qst, q_data)
