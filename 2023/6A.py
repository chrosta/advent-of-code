#!/usr/bin/python
###
# 6A.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce

copy = {}
data = [re.sub('^(Time|Distance): ', "", l.strip()).strip() for l in  sys.stdin.readlines()]
time = [int(s) for s in re.sub('\s+', " ", data[0]).split(' ')]
dist = [int(s) for s in re.sub('\s+', " ", data[1]).split(' ')]
outs = [0 for d in range(0, len(dist))]
print("---")
print(time)
print(dist)
print(outs)
print("---")

for i in range(0, len(time)):
    t = time[i]
    d = dist[i]
    r = range(1, (t + 1))
    for x in r:
        v = (len(r) - x) * x
        if v > d:
            print(x, len(r), v)
            outs[i] += 1
        
print("---")
print(outs)
print(reduce((lambda x, y: x * y), outs))

###
# 503424
###
