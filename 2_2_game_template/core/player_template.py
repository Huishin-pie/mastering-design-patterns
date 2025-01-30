from abc import ABC, abstractmethod
from typing import List

from models.card import Card
from .deck_template import DeckTemplate


class PlayerTemplate(ABC):

    def __init__(self, order: int):
        self.name = ""
        self.order = order
        self.cards: List[Card] = []

    def __str__(self):
        return f"Player name: {self.name}, Order: {self.order}"


    @abstractmethod
    def name_self(self):
        pass

    def get_hand_card(self, deck: DeckTemplate):
        self.cards.append(deck.draw_card())

    # uno need overwrite
    def can_play(self, deck: DeckTemplate) -> bool:
        return True

    @abstractmethod
    def select_play_card(self, deck: DeckTemplate) -> Card:
        pass

    def play_card(self, deck: DeckTemplate):
        played_card = self.select_play_card(deck)  # hook
        print(f"[{self}] - Played card: {played_card}")
        if not deck.accept_play(played_card):  # hook
            self.play_card(deck)
        else:
            self.cards.remove(played_card)

    @abstractmethod
    def can_not_play_action(self, deck: DeckTemplate):
        pass

    def take_turn(self, deck: DeckTemplate):
        if self.can_play(deck):  # hook()
            self.play_card(deck)
        else:
            self.can_not_play_action(deck)  # hook
