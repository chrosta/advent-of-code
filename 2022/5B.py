#!/usr/bin/python
###
# 5B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/5.text | ./5B.py 
###
import re, ast, sys
from itertools import groupby
lines = [l[:-1] for l in sys.stdin.readlines()]
stacks = [list(s.replace('   ','[.]').replace(' ','').replace('[','').replace(']','')) for s in lines if '[' in s]
stacks = list(zip(*stacks[::-1]))
stacks = [list(''.join(s).replace('.','')) for s in stacks]
moves = [[int(n) for n in re.sub(r'\s{2,}',' ',re.sub(r'[a-z]+','',m)).strip().split(' ')] for m in lines if 'move' in m]

for i in range(0,len(stacks)):
    print(i+1, stacks[i])
print("---")
for m in moves:
    print(m)
    f = stacks[m[1]-1]
    t = stacks[m[2]-1]
    x = f[(-1*m[0]):]
    stacks[m[1]-1] = f[0:(-1*m[0])]
    stacks[m[2]-1] += x
print("---")
for i in range(0,len(stacks)):
    print(i+1, stacks[i])
print("---")
print(''.join([s[-1:][0] for s in stacks if len(s) > 0]))
###
# QRQFHFWCL
###
