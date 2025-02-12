from typing import List, Union
from typing import Optional


from .validate_handler import ValidateHandler
from card.card import Card
from card_pattern.card_pattern import CardPattern
from card_pattern.pair_pattern import PairPattern


class PairValidate(ValidateHandler):

    def __init__(self, next: Optional[ValidateHandler]):
        super().__init__(next)
    
    def is_pair(self, cards: List[Card]) -> bool:
        if len(cards) != 2:  
            return False
        
        return cards[0].rank == cards[1].rank

    def match(self, cards: List[Card], top_play: Optional[CardPattern]) -> bool:
        if top_play is not None:
            return type(top_play) is PairPattern and self.is_pair(cards)
        else:
            return self.is_pair(cards)

    def handle(self, cards: List[Card], top_play: Optional[CardPattern])  -> Union[CardPattern, None]:
        new_card_pattern = PairPattern(cards)
        
        if top_play is None:
            return new_card_pattern
        
        if new_card_pattern > top_play:
            return new_card_pattern
        else:
            return None