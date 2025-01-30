from typing import List

from .deck_template import DeckTemplate
from models.showdown_card import ShowdownCard


class ShowdownDeck(DeckTemplate):
    CARDS_QTY = 52

    def __init__(self, cards: List[ShowdownCard]):
        super().__init__(cards)
        self.round_winner_order: List[int] = []


    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if len(value) == 0 or len(value) > self.CARDS_QTY:
            raise ValueError(
                f"The quantity of cards must equal {self.CARDS_QTY}.")
        self._cards = value

    def execute_turn(self):
        self.show_played_card()
        self.count_point()
        self.remove_played_card()
        pass

    def show_played_card(self):
        (print(played_card) for played_card in self.played_cards)

    def count_point(self):
        max_rank, max_suit = max(
            [(card.rank.value, card.suit.value) for card in self.played_cards])
        self.round_winner_order = [index + 1 for index, card in enumerate(self.played_cards) if card.rank.value ==
                                   max_rank and card.suit.value == max_suit]

    def remove_played_card(self):
        self.played_cards.clear()
