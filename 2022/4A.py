#!/usr/bin/python
###
# 4A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/4.text | ./4A.py 
###
import ast, sys
from itertools import groupby
lines = [l.strip() for l in sys.stdin.readlines()]
pairs = [l.split(',') for l in lines]
result = 0
for p in pairs:
    r = p[0].split('-')
    p[0] = [i for i in range(int(r[0]),int(r[1])+1)]
    r = p[1].split('-')
    p[1] = [i for i in range(int(r[0]),int(r[1])+1)]
for p  in pairs:
    t = 0
    try:
        x = [p[1].index(i) for i in p[0]]
        t = 1
    except: pass
    try:
        y = [p[0].index(i) for i in p[1]]
        t = 1
    except: pass
    if t > 0:
        print(p)
        result += 1
print(result)
###
# 507
###
