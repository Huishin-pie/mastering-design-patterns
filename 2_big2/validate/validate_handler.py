from abc import ABC, abstractmethod
from typing import List, Union
from typing import Optional


from card.card import Card
from card_pattern.card_pattern import CardPattern


class ValidateHandler(ABC):

    def __init__(self, next: Optional['ValidateHandler']):
        self.next = next
        
        
    def validate(self, cards: List[Card], top_play: CardPattern)  -> Union[CardPattern, None]:
        if self.match(cards, top_play):
            return self.handle(cards, top_play)
        elif self.next is not None:
            return self.next.validate(cards, top_play)

    @abstractmethod
    def match(self, cards: List[Card], top_play: Optional[CardPattern]) -> bool:
        pass

    @abstractmethod
    def handle(self, cards: List[Card], top_play: Optional[CardPattern])  -> Union[CardPattern, None]:
        pass