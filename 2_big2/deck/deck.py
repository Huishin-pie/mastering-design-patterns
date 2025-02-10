from typing import List
import random

from card.card import Card


class Deck():
    CARDS_QTY = 52

    def __init__(self, cards: List[Card]):
        self.cards = cards


    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if len(value) != self.CARDS_QTY:
            raise ValueError(
                f"The quantity of cards must equal {self.CARDS_QTY}.")
        self._cards = value

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Card:
        if not self.cards:
            raise ValueError("No card to get.")
        return self.cards.pop(-1)
