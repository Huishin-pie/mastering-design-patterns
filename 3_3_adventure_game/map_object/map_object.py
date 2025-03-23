from dataclasses import dataclass
from enum import Enum
from abc import ABC

class Symbol(Enum):
    TREASURE = 'x'
    OBSTACLE = '□'
    MONSTER = 'M'
    UP = '↑'
    RIGHT = '→'
    DOWN = '↓'
    LEFT = '←'

class Direction(Enum):
    UP = 'u'
    DOWN = 'd'
    LEFT = 'l'
    RIGHT = 'r'

@dataclass
class Position:
    x: int
    y: int

class MapObject(ABC):
    def __init__(self, symbol):
        self.symbol = symbol
        self.position = Position(0, 0)

    def __str__(self): 
        return self.symbol.value