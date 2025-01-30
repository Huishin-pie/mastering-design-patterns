from enum import Enum
from .card import Card


class Num(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


class Color(Enum):
    BLUE = "blue"
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"


class UnoCard(Card):

    def __init__(self, color: Color, num: Num):
        super().__init__()
        self.color = color
        self.num = num

    def __str__(self):
        return f"{self.color.value} {self.num.value}"
