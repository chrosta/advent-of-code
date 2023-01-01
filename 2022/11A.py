#!/usr/bin/python
###
# 11A.
# [chrosta@toolbox:~/Github/advent-of-code@chrosta/advent-of-code/2022]$ cat ./data/11.text | ./11A.py
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce

class Monkey:
    def __init__(self, number, items, oper, test):
        self.__number = number
        self.__items = items
        self.__oper = oper
        self.__test = test
        self.__monkeys = []
        self.__count = 0

    def __repr__(self):
        return str([self.__number, self.__items, self.__test, self.__monkeys[0].number(), self.__monkeys[1].number(), self.__count])

    def __str__(self):
        return str([self.__number, self.__items, self.__test, self.__monkeys[0].number(), self.__monkeys[1].number(), self.__count])

    def count(self):
        return self.__count

    def number(self):
        return self.__number

    def turn(self):
        while len(self.__items) > 0:
            old = self.__items.pop(0)
            new = eval(self.__oper.split(" = ")[1]) // 3
            if new % self.__test == 0:
                self.__monkeys[0].append_throwed_item(new)
            else:
                self.__monkeys[1].append_throwed_item(new)
            self.__count += 1
    
    def append_throwed_item(self, i):
        self.__items.append(i)

    def bind_to_monkeys(self, m):
        self.__monkeys = m

data = {}
lines = [l.strip().split(':') for l in sys.stdin.readlines()]
for l in lines:
    if "Monkey" in l[0]:
        number = int(l[0].split(' ')[1])
        continue
    if "Starting items" in l[0]:
        items = [int(i.strip()) for i in l[1].split(", ")]
        continue
    if "Operation" in l[0]:
        oper = l[1].strip()
        continue
    if "Test" in l[0]:
        test = int(l[1].split(' ')[3])
        continue
    if "If true" in l[0]:
        t = int(l[1].split(' ')[4])
        continue
    if "If false" in l[0]:
        f = int(l[1].split(' ')[4])
        continue
    if len(l[0]) == 0:
        data[number] = [items, oper, test, t, f]

monkeys = [Monkey(k, d[0], d[1], d[2]) for k, d in data.items()]
for m in monkeys:
    b = [n for n in data[m.number()][3:5]]
    m.bind_to_monkeys([monkeys[b[0]], monkeys[b[1]]])
    print(m)
print("---")

for r in range(0, 20):
    for m in monkeys:
        m.turn()
    for m in monkeys:
        print(m)
    print("---")

r = [m.count() for m in monkeys]
r.sort()
r = reduce(lambda x, y: x*y, r[-2:])
print(r)
###
# 108240
###
