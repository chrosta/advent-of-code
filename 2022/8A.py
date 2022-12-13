#!/usr/bin/python
###
# 8A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/8.text | ./8A.py 
###
import re, ast, sys
from itertools import groupby
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
            except KeyError: break
        #--
        if 1 in f:
            r += 1

print(r)
###
# 1796
###
