#!/usr/bin/python
###
# 2B.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce


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

o = 0
print('C:', colors)
for g in games:
    print("---")
    print(str(i)+':', g)
    r = {'r':0, 'g':0, 'b':0}
    for s in g:
        for c in "rgb":
            try: n = s[c]
            except KeyError: n = 0
            if n > r[c]: r[c] = n
    r = reduce(lambda x,y:x*y, [v for k,v in r.items()])
    print('R:', r)
    o += r
        
print("===")
print(o)

###
# 70387
###
