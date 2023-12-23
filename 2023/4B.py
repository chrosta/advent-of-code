#!/usr/bin/python
###
# 4B.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce

copy = {}
data = [re.sub('^Card ', "", l.strip()).strip() for l in  sys.stdin.readlines()]
for d in data:
    a, b = [x.strip() for x in d.split('|')]
    k, a = [x.strip() for x in a.split(':')]
    a = [int(m.group()) for m in re.finditer('\d+', a)]
    b = [int(m.group()) for m in re.finditer('\d+', b)]
    a.sort()
    b.sort()
    c = len([x for x in a if x in b])
    copy[int(k)] = [c, 0, 1]

i = 0
print(i, copy)
while True:
    i += 1
    loop = 0
    for k in copy:
        while copy[k][1] < copy[k][2]:
            for x in range(1, (copy[k][0] + 1)):
                copy[k + x][2] += 1
                loop += 1
            copy[k][1] += 1
    if loop == 0: break
    print(i, copy)

print("===")
print(sum([v[2] for k,v in copy.items()]))

###
# 8467762
###
