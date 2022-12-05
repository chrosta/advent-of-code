#!/usr/bin/python
###
# 2A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/2.text | ./2A.py 
###
import ast, sys
from itertools import groupby
my_shapes_score = {'X':1,'Y':2,'Z':3}
draws_combinations = ['AX','BY','CZ']
opponent_wins_combinations = [['AX','CZ'],['BY','AX'],['CZ','BY']]
rounds = [l.strip().replace(" ", "") for l in sys.stdin.readlines()]
result = 0
for r in rounds:
    if len([c for c in opponent_wins_combinations if r[0] in c[0] and r[1] in c[1]]) > 0:
        o = 0
    else:
        if r in draws_combinations:
            o = 3
        else:
            o = 6
    result += (o + my_shapes_score[r[1]])
print(result)
###
# 11666
###
