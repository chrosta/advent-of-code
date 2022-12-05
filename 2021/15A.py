#!/usr/bin/python
###
# 15A
###
import sys
from functools import reduce
from copy import deepcopy as dc
cavern = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".split('\n')
cavern = [[int(d) for d in list(c)] for c in cavern if len(c) > 0]
rows = len(cavern)
cols = len(cavern[0])
visited = []
#--
def show(t, d):
    print("---"+t+"---")
    print(str(d).replace('[[',"[").replace(']]', "]").replace(' ', "").replace('],[', "]\n[").replace('[', "").replace(']', "").replace("'", "").replace(',',""))
    print("---")
#--
class Node(object):
    def __init__(self, r, c, t):
        self.r = r
        self.c = c
        self.t = t + self.risk()

    def __str__(self):
        return str(f"[{self.r},{self.c}]({self.risk()})")

    def risk(self):
        global cavern
        return cavern[self.r][self.c]

    def total(self):
        global cavern
        return self.t - cavern[0][0]

    def next_neighbors(self):
        global visited
        global rows
        global cols
        if self.r == (rows-1) and self.c == (cols-1):
            print(self.total())
        else:
            m = {}
            if (self.c+1) < cols:
                n = Node(self.r, self.c+1, self.t)
                if str(n) not in [str(v) for v in visited]:
                    try: m[n.risk()].append(n)
                    except KeyError: m[n.risk()] = [n]
                    visited.append(n)
            if (self.r+1) < rows:
                n = Node(self.r+1, self.c, self.t)
                if str(n) not in [str(v) for v in visited]:
                    try: m[n.risk()].append(n)
                    except KeyError: m[n.risk()] = [n]
                    visited.append(n)
            #--
            for k, v in m.items():
                return v
#--
show("CAVERN", cavern)
n = Node(0, 0, 0)
visited.append(n)
queue = n.next_neighbors()
#--
print(queue)
while True:
    n = queue.pop(0)
    print(str(n))
    queue += n.next_neighbors()
