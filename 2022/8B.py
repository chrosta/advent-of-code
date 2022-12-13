#!/usr/bin/python
###
# 8B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/8.text | ./8B.py
###
import re, ast, sys
from itertools import groupby
from functools import reduce
data = [list(l.strip()) for l in sys.stdin.readlines()]
grid = {}

h = len(data)
w = len(data[0])
for y in range(0, h):
    print(data[y])
    for x in range(0, w):
        grid[(x, y)] = data[y][x]

r = 0
for y in range(0, h):
    for x in range(0, w):
        t = grid[(x, y)]
        f = [1, 1, 1, 1]
        v = [0, 0, 0, 0]
        #--
        # Check to UP:
        #--
        a = x
        b = y
        while True:
            b -= 1
            try:
                if t <= grid[(a, b)]:
                    f[0] = 0
                    v[0] += 1
                    break
                else:
                    v[0] += 1
            except KeyError: break
        #--
        # Check to RIGHT:
        #--
        a = x
        b = y
        while True:
            a += 1
            try:
                if t <= grid[(a, b)]:
                    f[1] = 0
                    v[1] += 1
                    break
                else:
                    v[1] += 1
            except KeyError: break
        #--
        # Check to DOWN:
        #--
        a = x
        b = y
        while True:
            b += 1
            try:
                if t <= grid[(a, b)]:
                    f[2] = 0
                    v[2] += 1
                    break
                else:
                    v[2] += 1
            except KeyError: break
        #--
        # Check to LEFT:
        #--
        a = x
        b = y
        while True:
            a -= 1
            try:
                if t <= grid[(a, b)]:
                    f[3] = 0
                    v[3] += 1
                    break
                else:
                    v[3] += 1
            except KeyError: break
        #--
        if 1 in f:
            c = reduce(lambda x, y: x*y, v)
            if c > r:
                r = c
            
print(r)
###
# 288120
###
