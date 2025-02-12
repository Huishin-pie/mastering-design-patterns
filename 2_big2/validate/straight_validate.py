from typing import List, Union
from typing import Optional


from .validate_handler import ValidateHandler
from card.card import Card
from card_pattern.card_pattern import CardPattern
from card_pattern.straight_pattern import StraightPattern


class StraightValidate(ValidateHandler):

    def __init__(self, next: Optional[ValidateHandler]):
        super().__init__(next)
        
    
    def is_straight(self, cards: List[Card]) -> bool:
        if len(cards) != 5:  
            return False
        
        sorted_cards = sorted(cards, key=lambda card: card.rank.value)

        for i in range(4):
            if sorted_cards[i + 1].rank.value != sorted_cards[i].rank.value + 1:
                return False

        return True

    def match(self, cards: List[Card], top_play: Optional[CardPattern]) -> bool:
        if top_play is not None:
            return type(top_play) is StraightPattern and self.is_straight(cards)
        else:
            return self.is_straight(cards)

    def handle(self, cards: List[Card], top_play: Optional[CardPattern])  -> Union[CardPattern, None]:
        new_card_pattern = StraightPattern(cards)
        
        if top_play is None:
            return new_card_pattern
        
        if new_card_pattern > top_play:
            return new_card_pattern
        else:
            return None