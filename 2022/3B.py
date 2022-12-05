#!/usr/bin/python
###
# 3B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/3.text | ./3B.py 
###
import ast, sys
from itertools import groupby
lp = "abcdefghijklmnopqrstuvwxyz"
hp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rucksacks = [l.strip() for l in sys.stdin.readlines()]
groups = [rucksacks[g:][:3] for g in range(0,len(rucksacks),3)]
result = 0
for g in groups:
    for l in lp:
        i = 0
        try:
            x = [b.index(l) for b in g]
            i = lp.index(l) + 1
            break
        except: pass
    for h in hp:
        j = 0
        try:
            x = [b.index(h) for b in g]
            j = hp.index(h) + 27
            break
        except: pass
    result += (i + j)
print(result)
###
# 2864
###
