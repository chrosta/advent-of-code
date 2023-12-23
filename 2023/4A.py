#!/usr/bin/python
###
# 4A.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce

r = 0
data = [re.sub('^.*:', "", l.strip()).strip() for l in  sys.stdin.readlines()]
for d in data:
    a, b = [x.strip() for x in d.split('|')]
    a = a.split(' ')
    c = []
    for x in a:
        if x in b.split(' '):
            try: c.append(int(x))
            except ValueError: pass
    if len(c) > 0:
        d = pow(2, len(c) - 1)
        print("---")
        print(c, d)
        r += d
        
print("===")
print(r)    

###
# 26346
###
