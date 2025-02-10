import copy

from .collision_handler import CollisionHandler


class SameType(CollisionHandler):

    def __init__(self, next: CollisionHandler):
        super().__init__(next)

    
    def handle(self, sprite1, sprite2, sprites):
        print('These are the same type.')
    
        return copy.deepcopy(sprites)

    def match(self, sprite1, sprite2):
        return type(sprite1) is type(sprite2) 