from abc import ABC
from typing import List


from card.card import Card


class CardPattern(ABC):

    def __init__(self, cards: List[Card]):
        self.cards = cards
