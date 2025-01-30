import copy

from .collision_handler import CollisionHandler
from sprite.hero import Hero
from sprite.fire import Fire


class HeroFire(CollisionHandler):

    def __init__(self, next: CollisionHandler):
        super().__init__(next)

    
    def handle(self, sprite1, sprite2, sprites):
        print('Handle hero and fire')

        new_sprites = copy.deepcopy(sprites)

        sprite1_copy = next((s for s in new_sprites if s.coord == sprite1.coord), None)
        sprite2_copy = next((s for s in new_sprites if s.coord == sprite2.coord), None)

        if sprite1_copy is None or sprite2_copy is None:
            return new_sprites

        if isinstance(sprite1_copy, Hero):
            if sprite1_copy.hp - 10 < 1:
                new_sprites.remove(sprite1_copy)
            else:
                sprite1_copy.hp -= 10
                sprite1_copy.coord = sprite2_copy.coord

            new_sprites.remove(sprite2_copy)

        elif isinstance(sprite2_copy, Hero):
            if sprite2_copy.hp - 10 < 1:
                new_sprites.remove(sprite2_copy)
            else:
                sprite2_copy.hp -= 10

            new_sprites.remove(sprite1_copy)

        return new_sprites

    def match(self, sprite1, sprite2):
        return (isinstance(sprite1, Hero) and isinstance(sprite2, Fire)) or (isinstance(sprite1, Fire) and isinstance(sprite2, Hero)) 