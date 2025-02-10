from typing import List


from .card_pattern import CardPattern
from card.card import Card


class PairPattern(CardPattern):
    CARDS_QTY = 2
    
    def __init__(self, cards: List[Card]):
        super().__init__(cards)
        
    
    def __str__(self):
        return f"對子 {' '.join(str(card) for card in self.cards)}"
    
    
    def __lt__(self, other: "PairPattern") -> bool:
        self_value = self.cards[0].rank.value
        other_value = other.cards[0].rank.value

        return self_value < other_value
        
        
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        if len(value) != self.CARDS_QTY:
            raise ValueError(f"The card size must be {self.CARDS_QTY}.")
        self._cards = value