#!/bin/usr/python

import sys
import json
import urllib.request
from pprint import pprint


class astro_table:
    def __init__(self, fields):
        self.r_margin = 1
        self.width = [2*self.r_margin + len(f) for f in fields]
        self.fields = fields
        self.data = []
        self.table = ''

    def add_item(self, item):
        tmp = [item[f] for f in self.fields]
        cur_width = [2*self.r_margin + len(t) for t in tmp]
        self.width = [max(
            self.width[i], cur_width[i]) for i in range(len(tmp))]
        self.data.append(tmp)

    def build(self):
        self.table = '+'
        for i in range(len(self.fields)):
            self.table += '-'*self.width[i] + '+'
        self.table += '\n|'
        for i, f in enumerate(self.fields):
            padding = max(0, self.width[i] - len(f) - self.r_margin)
            self.table += ' ' + f + ' '*padding + '|'
        self.table += '\n|'
        for i in range(len(self.fields)):
            self.table += '-'*self.width[i] + '|'
        for d in self.data:
            self.table += '\n|'
            for i, e in enumerate(d):
                padding = max(0, self.width[i] - len(e) - self.r_margin)
                self.table += ' ' + e + ' '*padding + '|'
        self.table += '\n+'
        for i in range(len(self.fields)):
            self.table += '-'*self.width[i] + '+'


url = "http://api.open-notify.org/astros.json"
d_json = json.loads(
        urllib.request.urlopen(url).read().decode("utf-8"))
# pprint(d_json)
a = astro_table(['name', 'craft'])
for p in d_json['people']:
    a.add_item(p)
a.build()
print(a.table)
