from map_object.map_object import MapObject, Symbol

class Obstacle(MapObject):
    def __init__(self):
        super().__init__(Symbol.OBSTACLE)