#!/usr/bin/python
###
# 1B.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby

nums = []
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
data = [l.strip() for l in  sys.stdin.readlines()]
for d in data:
    e = dc(d)
    f = dc(d)
    t = {}
    for w in words:
        for i in [m.start() for m in re.finditer(w, d)]:
            t[i] = w
    t = dict(sorted(t.items()))
    print(d, t)
    t = [v for k,v in t.items()]
    if len(t) > 0:
        t = [t[:1][0], t[-1:][0]]
        e = e.replace(t[0], str(words.index(t[0]) + 1))
        f = f.replace(t[1], str(words.index(t[1]) + 1))
    print(e)
    print(f)
    a = [m.group() for m in re.finditer('[a-z]*\d{1}', e)]
    a = a[:1][0][-1:]
    b = [m.group() for m in re.finditer('\d{1}[a-z]*', f)]
    b = b[-1:][0][:1]
    n = int(a + b)
    nums.append(n)
    print(n)
    print("---")
print(len(nums))
print(sum(nums))

###
# 55429
###
