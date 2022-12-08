#!/usr/bin/python
###
# 7B.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/7.text | ./7B.py 
###
import re, ast, sys
from itertools import groupby
lines = [l.strip() for l in sys.stdin.readlines()]
candidates = {}
total = 40532950

disk_space = 70000000
required_space = 30000000
wanting_space = required_space - (disk_space - total)
print(wanting_space)
print("---")
def process_the_directory_from_line(d, j):
    global candidates
    i = j
    s = 0
    print("DIR=", d)
    while True:
        try:
            l = lines[i]
        except IndexError:
            print("DIR=", d, "(" + str(s) + ")")
            candidates[d] = s
            return [s, i]
        c = l.split(' ')
        if c[0] == '$':
            if c[1] == "cd":
                if c[2] == "..":
                    print("DIR=", d, "(" + str(s) + ")")
                    candidates[d] = s
                    return [s, i]
                else:
                    t = process_the_directory_from_line((d + "/" + c[2]).replace("//", "/"), i+1)
                    s += t[0]
                    i = t[1]
        else:
            try:
                x = int(c[0])
                s += x
            except: pass
        i += 1

process_the_directory_from_line("/", 1)
print("---")
candidates = dict(sorted(candidates.items(), key=lambda item: item[1]))
candidates = [c for c in candidates.items() if c[1] >= wanting_space]
print(candidates[0][1])
###
# 545729
###
