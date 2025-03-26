from enum import Enum
from typing import TYPE_CHECKING

from map_object.map_object import MapObject, Symbol
from map_object.role import Role
from state.accelerated import Accelerated
from state.healing import Healing
from state.invincible import Invincible
from state.orderless import Orderless
from state.poisoned import Poisoned
from state.stockpile import Stockpile
from state.teleport import Teleport

if TYPE_CHECKING:
    from map.map import Map

class TreasureType(Enum):
    SUPER_STAR = "super_star"
    POISON = "poison"
    ACCELERATING_POTION = "accelerating_potion"
    HEALING_POTION = "healing_potion"
    DEVIL_FRUIT = "devil_fruit"
    KINGS_ROCK = "kings_rock"
    DOKODEMO_DOOR = "dokodemo_door"

class Treasure(MapObject):
    def __init__(self, type: TreasureType, map: "Map"):
        super().__init__(Symbol.TREASURE, map)
        self.type = type

    def touch_action(self, role: Role):
        if self.type == TreasureType.SUPER_STAR:
            return Invincible(role)
        elif self.type == TreasureType.POISON:
            return Poisoned(role)
        elif self.type == TreasureType.ACCELERATING_POTION:
            return Accelerated(role)
        elif self.type == TreasureType.HEALING_POTION:
            return Healing(role)
        elif self.type == TreasureType.DEVIL_FRUIT:
            return Orderless(role)
        elif self.type == TreasureType.KINGS_ROCK:
            return Stockpile(role)
        elif self.type == TreasureType.DOKODEMO_DOOR:
            return Teleport(role)