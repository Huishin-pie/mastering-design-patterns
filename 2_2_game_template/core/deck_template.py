from abc import ABC, abstractmethod
from typing import List
import random

from models.card import Card


class DeckTemplate(ABC):

    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.played_cards: List[Card] = []


    def shuffle(self):
        random.shuffle(self.cards)

    # uno need overwrite
    def draw_card(self):
        num = random.randint(0, len(self.cards)-1)
        return self.cards.pop(num)

    # uno need overwrite
    def accept_play(self, card: Card):
        self.played_cards.append(card)
        return True

    @abstractmethod
    def execute_turn(self):
        pass
