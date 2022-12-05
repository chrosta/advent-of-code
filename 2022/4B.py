#!/usr/bin/python
###
# 4B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/4.text | ./4B.py 
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
    try:
        x = [i for i in p[0] if i in p[1]]
    except: pass
    try:
        y = [i for i in p[1] if i in p[0]]
    except: pass
    if len(x) > 0 or len(y) > 0:
        result += 1
print(result)
###
# 897
###
