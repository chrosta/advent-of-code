#!/usr/bin/python
###
# 3A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/3.text | ./3A.py 
###
import ast, sys
from itertools import groupby
lp = "abcdefghijklmnopqrstuvwxyz"
hp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rucksacks = [l.strip() for l in sys.stdin.readlines()]
rucksacks = [[r[:int(len(r)/2)], r[int(len(r)/2):]] for r in rucksacks]
result = 0
for l in [[x for x in r[0] if x in r[1]][0] for r in rucksacks]:
    try:
        i = lp.index(l) + 1
    except:
        i = hp.index(l) + 27
    result += i
print(result)
###
# 8202
###
