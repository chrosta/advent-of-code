#!/usr/bin/python
###
# 9B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/9.text | ./9B.py
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce


def get_distance(a, b):
    x = 'x'
    y = 'y'
    d = {'x':a[x] - b[x], 'y':a[y] - b[y]}
    return d

r = []
x = 'x'
y = 'y'
nodes = [{x:0, y:0} for i in range(0,10)]
moves = [l.strip().split(' ') for l in sys.stdin.readlines()]
for m in moves:
    m[1] = int(m[1])
    for s in range(0, m[1]):
        #--
        # Move to RIGHT:
        #--
        if m[0] == 'R': nodes[0][x] += 1
        #--
        # Move to UP:
        #--
        if m[0] == 'U': nodes[0][y] += 1
        #--
        # Move to LEFT:
        #--
        if m[0] == 'L': nodes[0][x] -= 1
        #--
        # Move to DOWN:
        #--
        if m[0] == 'D': nodes[0][y] -= 1
        #--
        for p in [nodes[i:i+2] for i in range(0, len(nodes)) if len(nodes) - i > 1]:
            d = get_distance(p[0], p[1])
            if d[x] > 1:
                p[1][x] = p[0][x] - 1
                p[1][y] = p[0][y]
                continue
            if d[y] > 1:
                p[1][x] = p[0][x]
                p[1][y] = p[0][y] - 1
                continue
            if d[x] < -1:
                p[1][x] = p[0][x] + 1
                p[1][y] = p[0][y]
                continue
            if d[y] < -1:
                p[1][x] = p[0][x]
                p[1][y] = p[0][y] + 1
                continue
        #--
        print(str(nodes).replace("'x'", "x").replace("'y'", "y").replace(": ", ":"))
        n = dc(nodes[len(nodes) - 1])
        if n not in r: r.append(n)
    print("---")
print(r, "=>", len(r))
###
# 2627
###
