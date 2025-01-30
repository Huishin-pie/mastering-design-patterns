import random

from .showdown_player import ShowdownPlayer
from .showdown_deck import ShowdownDeck


class ShowdownAIPlayer(ShowdownPlayer):
    NAME_LIST = ["Andy", "Bob", "Lisa", "Rose"]

    def __init__(self, order: int):
        super().__init__(order)


    def name_self(self):
        self.name = f"AI {random.choice(self.NAME_LIST)}"

    def select_play_card(self, deck: ShowdownDeck):
        return random.choice(self.cards)
