#!/usr/bin/python
###
# 3A.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce


r = []
data = [l.strip() for l in  sys.stdin.readlines()]
for i in range(0, len(data)):
    b = ""
    n = ""
    d = data[i];
    if i > 0: b = data[i-1]
    if (i+1) < len(data): n = data[i+1]
    print("---")
    print([b, d, n])
    matches = [m for m in re.finditer('\d+', d)]
    for m in matches:
        g = m.group()
        s = m.start()
        e = m.end()
        o = []
        if s > 0: s -= 1
        if e < len(d): e += 1
        if len(b) > 0: o.append(b[s:e])
        o.append(d[s:e])
        if len(n) > 0: o.append(n[s:e])
        if len([re.sub('\d', "", t).replace('.', "") for t in o if len(re.sub('\d', "", t).replace('.', "")) > 0]) > 0:
            print(g, o)
            r.append(int(g))
    print("---")

print(sum(r))

###
# 527144
###
