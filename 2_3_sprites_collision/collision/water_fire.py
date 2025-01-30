import copy

from .collision_handler import CollisionHandler
from sprite.water import Water
from sprite.fire import Fire


class WaterFire(CollisionHandler):

    def __init__(self, next: CollisionHandler):
        super().__init__(next)

    
    def handle(self, sprite1, sprite2, sprites):
        print('Handle water and fire')
        
        new_sprites = copy.deepcopy(sprites)

        sprite1_copy = next((s for s in new_sprites if s.coord == sprite1.coord), None)
        sprite2_copy = next((s for s in new_sprites if s.coord == sprite2.coord), None)

        if sprite1_copy is None or sprite2_copy is None:
            return new_sprites

        new_sprites.remove(sprite1_copy)
        new_sprites.remove(sprite2_copy)

        return new_sprites

    def match(self, sprite1, sprite2):
        return (isinstance(sprite1, Water) and isinstance(sprite2, Fire)) or (isinstance(sprite1, Fire) and isinstance(sprite2, Water)) 