from typing import TYPE_CHECKING

from map_object.map_object import MapObject, Symbol

if TYPE_CHECKING:
    from map.map import Map

class Obstacle(MapObject):
    def __init__(self, map: "Map"):
        super().__init__(Symbol.OBSTACLE, map)