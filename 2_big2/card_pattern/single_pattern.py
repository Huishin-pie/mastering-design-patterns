from typing import List


from .card_pattern import CardPattern
from card.card import Card


class SinglePattern(CardPattern):
    CARDS_QTY = 1
    
    def __init__(self, cards: List[Card]):
        super().__init__(cards) 
     
     
    def __str__(self):
        return f"單張 {' '.join(str(card) for card in self.cards)}" 
        
        
    def __lt__(self, other: "SinglePattern") -> bool:
        self_value = self.cards[0].rank.value
        self_suit = self.cards[0].suit.value
        other_value = other.cards[0].rank.value
        other_suit = other.cards[0].suit.value

        if self_value != other_value:
            return self_value < other_value
        return self_suit < other_suit
    
    
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        if len(value) != self.CARDS_QTY:
            raise ValueError(f"The card size must be {self.CARDS_QTY}.")
        self._cards = value 