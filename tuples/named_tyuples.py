from collections import namedtuple

Card = namedtuple('Card', 'rank suit')

SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')

def card_gen():
    for suit in SUITS:
        for rank in RANKS:
            card = Card(rank, suit)
            yield card


# for card in card_gen():
#     print(card)

#=====================================


class CardDeck:
    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __iter__(self):
        return CardDeck.card_gen()

    @staticmethod
    def card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in CardDeck.RANKS:
                card = Card(rank, suit)
                yield card

    @staticmethod
    def reversed_card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in reversed(CardDeck.RANKS):
                card = Card(rank, suit)
                yield card


print(list(CardDeck()))