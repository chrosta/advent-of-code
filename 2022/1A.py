#!/usr/bin/python
###
# 1A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/1.text | ./1A.py 
###
import ast, sys
from itertools import groupby
data = ast.literal_eval(str([list(group) for k, group in groupby([l.strip() for l in sys.stdin.readlines()], lambda x: x == "") if not k]).replace("'", ""))
sums = [sum(d) for d in data]
sums.sort()
print(sums[-1:])
###
# 68787
###
