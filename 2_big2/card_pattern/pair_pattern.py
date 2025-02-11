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
        self_max_suit = max(self.cards[0].suit.value, self.cards[1].suit.value)
        other_max_suit = max(other.cards[0].suit.value, other.cards[1].suit.value)

        return (self.cards[0].rank.value, self_max_suit) < (other.cards[0].rank.value, other_max_suit)
        
        
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        if len(value) != self.CARDS_QTY:
            raise ValueError(f"The card size must be {self.CARDS_QTY}.")
        self._cards = value