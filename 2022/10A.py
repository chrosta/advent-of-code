#!/usr/bin/python
###
# 10A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/10.text | ./10A.py
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce

total = 0
instruction = {'noop':1, 'addx':2}
program = [l.strip().split(' ') for l in sys.stdin.readlines()]
cycle = [{'counter':0, 'register':1, 'instruction':'', 'value':0, 'signal':0}]
breaks = [20, 60, 100, 140, 180, 220]
for p in program:
    cycle += [dc(cycle[-1:][0])]
    c = cycle[-1:][0]
    for i in range(0, instruction[p[0]]):
        c['counter'] += 1
        c['instruction'] = p[0]
        c['signal'] = c['counter'] * c['register']
        if c['counter'] in breaks:
            print(c)
            total += c['signal']
    try:
        c['value'] = int(p[1])
    except IndexError: c['value'] = 0
    c['register'] += c['value']
print("---")
print(total)
###
# 12560
###
