import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

"""
  通过实现__len__和__getitem__这两个特殊方法，
  FrenchDeck就可以使用random.choice、reversed和sorted方法,
  对合成的运算使得 __len__ 和 __getitem__ 的具体实现代理给 self._cards
  
  目前FrenchDeck是不能洗牌的，因为该类是不可变的，需实现 __setitem__方法
"""


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    deck = FrenchDeck()
    length = len(deck)

    card = choice(deck)
    print(length)
    for i in range(10):
        card = choice(deck)
        print(card)
    cards = deck[0:10]
    print(cards)
    for card in reversed(deck):
        print(card)

    for card in sorted(deck, key=spades_high):
        print(card)
