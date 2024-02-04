#!/usr/bin/python
###
# 7A.
###
import re, ast, sys
from copy import deepcopy as dc
from itertools import groupby
from functools import reduce
from libs.card_7a import Card
from libs.hand_7a import Hand


data = [l.strip() for l in  sys.stdin.readlines()]
hands_list = [d.split(' ')[0] for d in data]
their_bids = [d.split(' ')[1] for d in data]
ranks = {'HC':[], 'OP':[], 'TP':[], '3K':[], 'FH':[], '4K':[], '5K':[]}
hands = []

for i in range(0, len(hands_list)):
    h = Hand([Card(c) for c in hands_list[i]], their_bids[i])
    ranks[h.rank()].append(h)
    ranks[h.rank()].sort()

for k,r in ranks.items():
    for h in r:
        hands.append(h)

print(hands)
print([str(hands[i].bid()) + "*" + str(i+1) for i in range(0, len(hands))])
print("---")
print(sum([hands[i].bid()*(i+1) for i in range(0, len(hands))]))

###
# 251029473
###
