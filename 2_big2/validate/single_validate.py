from typing import List, Union
from typing import Optional


from .validate_handler import ValidateHandler
from card.card import Card
from card_pattern.card_pattern import CardPattern
from card_pattern.single_pattern import SinglePattern


class SingleValidate(ValidateHandler):

    def __init__(self, next: Optional[ValidateHandler]):
        super().__init__(next)
        
    
    def is_single(self, cards: List[Card]):
        return len(cards) == 1

    def match(self, cards: List[Card], top_play: Optional[CardPattern]) -> bool:
        if top_play is not None:
            return type(top_play) is SinglePattern and self.is_single(cards)
        else:
            return self.is_single(cards)

    def handle(self, cards: List[Card], top_play: Optional[CardPattern])  -> Union[CardPattern, None]:
        new_card_pattern = SinglePattern(cards)
        
        if top_play is None:
            return new_card_pattern
        
        print(new_card_pattern, top_play, new_card_pattern > top_play)
        
        if new_card_pattern > top_play:
            return new_card_pattern
        else:
            return None