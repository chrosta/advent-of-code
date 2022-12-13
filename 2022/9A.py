#!/usr/bin/python
###
# 9A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/9.text | ./9A.py
###
import re, ast, sys
from itertools import groupby
from functools import reduce
data = [l.strip().split(' ') for l in sys.stdin.readlines()]
tail = {}

def check_distance(h, t):
    x = 'x'
    y = 'y'
    if abs(h[x] - t[x]) > 1 or abs(h[y] - t[y]) > 1: return True
    return False

r = []
x = 'x'
y = 'y'
head = {x:0, y:0}
tail = {x:0, y:0}
for d in data:
    d[1] = int(d[1])
    for c in range(0, d[1]):
        #--
        # Move to RIGHT:
        #--
        if d[0] == 'R':
            head[x] += 1
            if check_distance(head, tail):
                tail[x] = head[x] - 1
                tail[y] = head[y]
        #--
        # Move to UP:
        #--
        if d[0] == 'U':
            head[y] += 1
            if check_distance(head, tail):
                tail[x] = head[x]
                tail[y] = head[y] - 1
        #--
        # Move to LEFT:
        #--
        if d[0] == 'L':
            head[x] -= 1
            if check_distance(head, tail):
                tail[x] = head[x] + 1
                tail[y] = head[y]
        #--
        # Move to DOWN:
        #--
        if d[0] == 'D':
            head[y] -= 1
            if check_distance(head, tail):
                tail[x] = head[x]
                tail[y] = head[y] + 1
        #--
        e = (tail[x], tail[y])
        if e not in r:
            r.append(e)
        #--
        print(str([head, tail]).replace("'x'", "x").replace("'y'", "y").replace(": ", ":"))
print(len(r))
###
# 6357
###
