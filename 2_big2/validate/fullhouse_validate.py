from typing import List, Union
from typing import Optional
from collections import Counter


from .validate_handler import ValidateHandler
from card.card import Card
from card_pattern.card_pattern import CardPattern
from card_pattern.fullhouse_pattern import FullhousePattern


class FullhouseValidate(ValidateHandler):

    def __init__(self, next: Optional[ValidateHandler]):
        super().__init__(next)
        
    
    def is_fullhouse(self, cards: List[Card]) -> bool:
        if len(cards) != 5:  
            return False

        rank_counts = Counter(card.rank.value for card in cards)
        counts = sorted(rank_counts.values())

        return counts == [2, 3]

    def match(self, cards: List[Card], top_play: Optional[CardPattern]) -> bool:
        if top_play is not None:
            return type(top_play) is FullhousePattern and self.is_fullhouse(cards)
        else:
            return self.is_fullhouse(cards)

    def handle(self, cards: List[Card], top_play: Optional[CardPattern])  -> Union[CardPattern, None]:
        new_card_pattern = FullhousePattern(cards)
        
        if top_play is None:
            return new_card_pattern
        
        if new_card_pattern > top_play:
            return new_card_pattern
        else:
            return None