import random

from .uno_player import UnoPlayer
from .uno_deck import UnoDeck


class UnoAIPlayer(UnoPlayer):
    NAME_LIST = ["Andy", "Bob", "Lisa", "Rose"]

    def __init__(self, order: int):
        super().__init__(order)


    def name_self(self):
        self.name = f"AI {random.choice(self.NAME_LIST)}"

    def select_play_card(self, deck: UnoDeck):
        playable_cards = self.get_can_play_cards(deck)
        return random.choice(list(playable_cards.values()))
