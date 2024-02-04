import functools
from functools import total_ordering


class Hand:

    def __init__(self, cards, bid):
        self.__bid = int(bid)
        self.__cards = cards


    def __lt__(self, hand):
        for i in range(0, len(self.__cards)):
            a = self.card(i)
            b = hand.card(i)
            if a != b:
                if a < b: return True
                else: break
        return False


    def __gt__(self, hand):
        for i in range(0, len(self.__cards)):
            a = self.card(i)
            b = hand.card(i)
            if a != b:
                if a > b: return True
                else: break
        return False


    def __le__(self, hand):
        for i in range(0, len(self.__cards)):
            a = self.card(i)
            b = hand.card(i)
            if a != b:
                if a <= b: return True
                else: break
        return False


    def __ge__(self, hand):
        for i in range(0, len(self.__cards)):
            a = self.card(i)
            b = hand.card(i)
            if a != b:
                if a >= b: return True
                else: break
        return True


    def __eq__(self, hand):
        for i in range(0, len(self.__cards)):
            a = self.card(i)
            b = hand.card(i)
            if a != b: return False
        return True


    def __repr__(self):
        s = ""
        for c in self.__cards:
            s += str(c).split('=')[0]
        return s + "=" + str(self.total())
 

    def bid(self):
        return self.__bid


    def card(self, index):
        return self.__cards[index]


    def rank(self):
        cards = str(self).split('=')[0]
        t = [x for x in [cards.count(c) for c in cards] if x > 1]
        if sum(t) == 0: return 'HC'
        if sum(t) == 4: return 'OP'
        if sum(t) == 8: return 'TP'
        if sum(t) == 9: return '3K'
        if sum(t) == 13: return 'FH'
        if sum(t) == 16: return '4K'
        if sum(t) == 25: return '5K'
        return 'XX'


    def total(self):
        t = 0
        for c in self.__cards:
            t += c.value()
        return t
