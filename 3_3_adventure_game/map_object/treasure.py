from enum import Enum

from map_object.map_object import MapObject, Symbol

class TreasureType(Enum):
    SUPER_STAR = "super_star"
    POISON = "poison"
    ACCELERATING_POTION = "accelerating_potion"
    HEALING_POTION = "healing_potion"
    DEVIL_FRUIT = "devil_fruit"
    KINGS_ROCK = "kings_rock"
    DOKODEMO_DOOR = "dokodemo_door"

class Treasure(MapObject):
    def __init__(self, type: TreasureType):
        super().__init__(Symbol.TREASURE)
        self.type = type

    def touch_action(self):
        return self.type