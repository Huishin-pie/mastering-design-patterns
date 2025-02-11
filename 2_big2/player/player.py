from abc import ABC, abstractmethod
from typing import List, Union
import re

from card.card import Card


class Player(ABC):

    def __init__(self, order: int):
        self.name = ""
        self.order = order
        self.hand_cards: List[Card] = []


    def __str__(self):
        return f"{self.name}"
    

    def _is_valid(self, text: str) -> bool:
        return bool(re.fullmatch(r"[A-Za-z0-9\u4e00-\u9fff]+", text))

    @abstractmethod
    def name_self(self):
        pass

    @abstractmethod
    def play_or_pass(self) -> Union[List[Card], None]:
        pass
