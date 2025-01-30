from enum import Enum
from .card import Card


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3


class ShowdownCard(Card):

    def __init__(self, rank: Rank, suit: Suit):
        super().__init__()
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.suit.name} {self.rank.value}"
