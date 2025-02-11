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
        self_max_card = max(self.cards, key=lambda card: card.rank.value)
        other_max_card = max(other.cards, key=lambda card: card.rank.value)
        
        if self_max_card.rank.value != other_max_card.rank.value:
            return self_max_card.rank.value < other_max_card.rank.value
        return self_max_card.suit.value < other_max_card.suit.value
        
        
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        if len(value) != self.CARDS_QTY:
            raise ValueError(f"The card size must be {self.CARDS_QTY}.")
        self._cards = value