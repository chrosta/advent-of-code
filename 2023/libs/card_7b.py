import functools
from functools import total_ordering


@total_ordering
class Card:
    VALUES = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


    def __init__(self, symbol):
        self.__symbol = symbol


    def __lt__(self, card):
        return Card.VALUES.index(self.__symbol) < card.value()


    def __gt__(self, card):
        return Card.VALUES.index(self.__symbol) > card.value()

    
    def __le__(self, card):
        return Card.VALUES.index(self.__symbol) <= card.value()


    def __ge__(self, card):
        return Card.VALUES.index(self.__symbol) >= card.value()


    def __eq__(self, card): 
        return Card.VALUES.index(self.__symbol) == card.value()


    def __repr__(self):
        return self.__symbol + "=" + str(self.value())
 

    def value(self):
        return Card.VALUES.index(self.__symbol)
