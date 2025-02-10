from typing import List
from collections import Counter


from .card_pattern import CardPattern
from card.card import Card


class FullhousePattern(CardPattern):
    CARDS_QTY = 5
    
    def __init__(self, cards: List[Card]):
        super().__init__(cards)
        
        
    def __str__(self):
        return f"葫蘆 {' '.join(str(card) for card in self.cards)}"
        
    
    def __lt__(self, other: "FullhousePattern") -> bool:
        # self_values = Counter(card.rank.value for card in self.cards)
        # other_values = Counter(card.rank.value for card in other.cards)
        
        #todo
        pass
        
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        if len(value) != self.CARDS_QTY:
            raise ValueError(f"The card size must be {self.CARDS_QTY}.")
        self._cards = value  