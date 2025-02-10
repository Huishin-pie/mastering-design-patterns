from abc import ABC, abstractmethod
from typing import List, Union

from card.card import Card


class Player(ABC):

    def __init__(self, order: int):
        self.name = ""
        self.order = order
        self.hand_cards: List[Card] = []


    def __str__(self):
        return f"{self.name}"


    @abstractmethod
    def name_self(self):
        pass

    @abstractmethod
    def play_or_pass(self) -> Union[List[Card], None]:
        pass
