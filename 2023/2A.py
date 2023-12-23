#!/usr/bin/python
###
# 2A.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby

games = []
colors = {'r':12, 'g':13, 'b':14}
data = [l.strip().replace("Game ", "") for l in  sys.stdin.readlines()]
for d in data:
    d = d.split(':')
    i = d[0]
    g = [j.strip() for j in d[1].strip().replace(', ', ",").split(';')]
    d = [k.split(',') for k in g]
    e = [] 
    for y in d:
        l = {}
        for z in y:
            k = z.split(' ')
            k.reverse()
            k[0] = k[0][:1]
            l[k[0]] = int(k[1])
        e.append(l)
    games.append(e)

i = 0
r = []
print('C:', colors)
for g in games:
    i += 1
    rg = []
    print("---")
    print(str(i)+':', g)
    for s in g:
        rs = []
        for c in "rgb":
            try: n = s[c]
            except KeyError: n = 0
            rs.append(n <= colors[c])
        rg.extend(rs)
    if False not in rg:
        r.append(i)

print("===")
print('R:', sum(r))

###
# 1734
###
