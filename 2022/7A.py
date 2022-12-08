#!/usr/bin/python
###
# 7A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/7.text | ./7A.py 
###
import re, ast, sys
from itertools import groupby
lines = [l.strip() for l in sys.stdin.readlines()]
total = 0

def process_the_directory_from_line(d, j):
    global total
    i = j
    s = 0
    print("DIR=", d)
    while True:
        try:
            l = lines[i]
        except IndexError:
            print("DIR=", d, "(" + str(s) + ")")
            if s < 100000:
                total += s
            return [s, i]
        c = l.split(' ')
        if c[0] == '$':
            if c[1] == "cd":
                if c[2] == "..":
                    print("DIR=", d, "(" + str(s) + ")")
                    if s < 100000:
                        total += s
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
print(total)
###
# 1423358
###
