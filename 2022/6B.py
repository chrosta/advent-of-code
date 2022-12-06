#!/usr/bin/python
###
# 6B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/6.text | ./6B.py 
###
import re, ast, sys
from itertools import groupby
stream = [l.strip() for l in sys.stdin.readlines()][0]
frames = [stream[s:s+14] for s in range(0, len(stream)) if len(stream) - s > 13]
print([stream.index(f)+len(f) for f in frames if len(f) == len(list(dict.fromkeys(f)))][0])
###
# 3605
###
