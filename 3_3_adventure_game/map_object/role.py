from abc import abstractmethod
from enum import Enum
from typing import TYPE_CHECKING

from map_object.map_object import MapObject

if TYPE_CHECKING:
    from map.map import Map

class State(Enum):
    NORMAL = "normal"
    INVINCIBLE = "invincible"
    POISONED = "poisoned"
    ACCELERATED = "accelerated"
    HEALING = "healing"
    ORDERLESS = "orderless"
    STOCKPILE = "stockpile"
    ERUPTING = "erupting"
    TELEPORT = "Teleport"

class Role(MapObject):
    def __init__(self, HP, attack_power, attack_range, symbol):
        super().__init__(symbol)
        self.HP = HP
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.state = State.NORMAL
        self.state_time = None

    @abstractmethod
    def take_turn(self, map: "Map"):
        pass

    @abstractmethod
    def attack(self, map: "Map"):
        pass

    def take_damage(self, damage: int):
        self.HP -= damage
        if self.HP < 0:
            self.HP = 0

    def heal(self, heal: int):
        self.HP += heal

    def is_alive(self):
        return self.HP > 0
    
    def change_state(self, state, state_time):
        self.state = state
        self.state_time = state_time

