#!/usr/bin/python
###
# 6B.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce

copy = {}
data = [re.sub('^(Time|Distance): ', "", l.strip()).strip() for l in  sys.stdin.readlines()]
time = int(''.join([str(int(s)) for s in re.sub('\s+', " ", data[0]).split(' ')]))
dist = int(''.join([str(int(s)) for s in re.sub('\s+', " ", data[1]).split(' ')]))
outs = 0
print("---")
print(time)
print(dist)
print(outs)
t = time
d = dist
r = range(1, (t + 1))
for x in r:
    v = (len(r) - x) * x
    if v > d:
        outs += 1
print("---")
print(outs)

###
# 32607562
###
