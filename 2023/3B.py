#!/usr/bin/python
###
# 3B.
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
    matches = [m for m in re.finditer('\*', d)]
    for m in matches:
        g = m.group()
        s = m.start()
        e = m.end()
        if s > 0: s -= 1
        if e < len(d): e += 1
        p = [a for a in range(m.start()-1, m.end()+1) if a >= 0 and a < len(d)]
        p = [p[0], p[-1:][0]+1]
        print('G:', m, p)
        o = []
        for l in [b, d, n]:
            for c in [x for x in re.finditer('\d+', l)]:
                print('C:', c)
                if c.start() in range(p[0], p[1]) or c.end() in range(p[0]+1, p[1]):
                    print('C:', c)
                    o.append(int(c.group()))
        if len(o) == 2:
            print(o)
            r.append(reduce(lambda x,y: x*y, o))
    print("---")

print(sum(r))

###
# 81463996
###
