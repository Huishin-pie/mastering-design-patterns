from typing import List


from .card_pattern import CardPattern
from card.card import Card


class StraightPattern(CardPattern):
    CARDS_QTY = 5
    
    def __init__(self, cards: List[Card]):
        super().__init__(cards)
        

    def __str__(self):
        return f"順子 {' '.join(str(card) for card in self.cards)}" 
        
    
    def __lt__(self, other: "StraightPattern") -> bool:
        self_values = [card.rank.value for card in self.cards]
        other_values = [card.rank.value for card in other.cards]

        self_max_value = max(self_values)
        other_max_value = max(other_values)

        return self_max_value < other_max_value
        
        
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        if len(value) != self.CARDS_QTY:
            raise ValueError(f"The card size must be {self.CARDS_QTY}.")
        self._cards = value