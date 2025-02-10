import random
from typing import List, Union

from .player import Player
from card.card import Card


class AIPlayer(Player):
    NAME_LIST = ["Andy", "Bob", "Lisa", "Rose"]

    def __init__(self, order: int):
        super().__init__(order)


    def name_self(self):
        self.name = f"AI {random.choice(self.NAME_LIST)}"

    def play_or_pass(self) -> Union[List[Card], None]:
        #todo
        pass
