#!/usr/bin/python
###
# 7B.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce
from libs.card_7b import Card
from libs.hand_7b import Hand
import numpy as np


data = [l.strip() for l in  sys.stdin.readlines()]
hands_list = [d.split(' ')[0] for d in data]
their_bids = [d.split(' ')[1] for d in data]
ranks = {'HC':[], 'OP':[], 'TP':[], '3K':[], 'FH':[], '4K':[], '5K':[]}
hands = []


print("---")
for i in range(0, len(hands_list)):
    h = hands_list[i]
    b = their_bids[i]
    h = list(h)
    t = list(np.unique(h))
    try: t.remove('J')
    except: pass
    h = ''.join(h)
    t = ''.join(t)
    v = []
    if 'J' in h:
        for j in t:
            c = [Card(k) for k in h.replace('J', j)]
            c.sort(reverse=True)
            v.append(Hand(c, b))
            v = sorted(v, key=lambda x: x.poker_rank(), reverse=True)
    print('->', v)
    h = Hand([Card(k) for k in h], b)
    try: v = v[0]
    except IndexError: v = h
    ranks[v.rank()].append(h)
    ranks[v.rank()].sort()
    print(h, '->', v, '->', ranks)

print("---")
for k,r in ranks.items():
    for h in r:
        hands.append(h)
print(hands)
print([str(hands[i].bid()) + "*" + str(i+1) for i in range(0, len(hands))])
print("---")
print(sum([hands[i].bid()*(i+1) for i in range(0, len(hands))]))

###
# 251003917
###
