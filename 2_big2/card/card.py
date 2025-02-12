from abc import ABC
from enum import Enum


class Rank(Enum):
    THREE = (3, "3")
    FOUR = (4, "4")
    FIVE = (5, "5")
    SIX = (6, "6")
    SEVEN = (7, "7")
    EIGHT = (8, "8")
    NINE = (9, "9")
    TEN = (10, "10")
    JACK = (11, "J")
    QUEEN = (12, "Q")
    KING = (13, "K")
    ACE = (14, "A")
    TWO = (15, "2")

    def __init__(self, value, display):
        self._value_  = value
        self.display = display 
        
        
    @classmethod
    def from_display(self, value):
        for rank in self:
            if rank.display == value:
                return rank
        return None


class Suit(Enum):
    CLUB = (0, "C")
    DIAMOND = (1, "D")
    HEART = (2, "H")
    SPADE = (3, "S")
    
    def __init__(self, value, display):
        self._value_  = value
        self.display = display 
        
        
    @classmethod
    def from_display(self, value):
        for suit in self:
            if suit.display == value:
                return suit
        return None


class Card(ABC):

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    
    def __str__(self):
        return f"{self.suit.display}[{self.rank.display}]"