#!/usr/bin/python
###
# 2B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/2.text | ./2B.py 
###
import ast, sys
from itertools import groupby
score = ['X','Y','Z']
wins = {'A':'Y','B':'Z','C':'X'}
draws = {'A':'X','B':'Y','C':'Z'}
losts = {'A':'Z','B':'X','C':'Y'}
rounds = [l.strip().replace(" ", "") for l in sys.stdin.readlines()]
result = 0
for r in rounds:
    if r[1] == 'Y':
        o = 3
        s = (score.index(draws[r[0]])+1)
    if r[1] == 'X':
        o = 0
        s = (score.index(losts[r[0]])+1)
    if r[1] == 'Z':
        o = 6
        s = (score.index(wins[r[0]])+1)
    result += (s + o)
print(result)
###
# 12767
###
