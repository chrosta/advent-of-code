#!/usr/bin/python
###
# 1A.
###
import re, ast, sys
from itertools import groupby

nums = []
data = [l.strip() for l in  sys.stdin.readlines()]
for d in data:
    print(d)
    a = [m.group() for m in re.finditer('[a-z]*\d{1}', d)]
    a = a[:1][0][-1:]
    b = [m.group() for m in re.finditer('\d{1}[a-z]*', d)]
    b = b[-1:][0][:1]
    i = int(a + b)
    nums.append(i)
    print(i)
    print("---")
print(sum(nums))

###
# 54605
###
