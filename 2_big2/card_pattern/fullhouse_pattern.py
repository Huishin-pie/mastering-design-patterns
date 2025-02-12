from typing import List


from .card_pattern import CardPattern
from card.card import Card


class FullhousePattern(CardPattern):
    CARDS_QTY = 5
    
    def __init__(self, cards: List[Card]):
        super().__init__(cards)
        
        
    def __str__(self):
        return f"葫蘆 {' '.join(str(card) for card in self.cards)}"
        
    
    def __lt__(self, other: "FullhousePattern") -> bool:
        self_dict = {}
        for card in self.cards:
            if card.rank.display not in self_dict:
                self_dict[card.rank.display] = [card]
            else:
                self_dict[card.rank.display].append(card)
                
        other_dict = {}
        for card in other.cards:
            if card.rank.display not in other_dict:
                other_dict[card.rank.display] = [card]
            else:
                other_dict[card.rank.display].append(card)
            
        self_three = None
        for rank, cards in self_dict.items():
            if len(cards) == 3:
                self_three = cards
                
        other_three = None
        for rank, cards in other_dict.items():
            if len(cards) == 3:
                other_three = cards
            
        self_max_card = max(self_three, key=lambda card: card.rank.value)
        other_max_card = max(other_three, key=lambda card: card.rank.value)
        
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