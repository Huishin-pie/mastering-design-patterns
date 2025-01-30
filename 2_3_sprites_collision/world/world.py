from typing import List
import random

from sprite.sprite import Sprite
from sprite.hero import Hero
from sprite.fire import Fire
from sprite.water import Water
from collision.collision_handler import CollisionHandler


class World:
    MAX_LENGTH = 30

    def __init__(self, collision_handler: CollisionHandler):
        self.collision_handler = collision_handler
        self.length: int = self.MAX_LENGTH
        self.sprites: List[Sprite] = self._create_sprites()


    def _create_sprites(self) -> List[Sprite]:
        available_coords = list(range(self.length))
        random.shuffle(available_coords)
        sprites = [
            Hero('H', available_coords.pop()),
            Hero('H', available_coords.pop()),
            Hero('H', available_coords.pop()),
            Water('W', available_coords.pop()),
            Water('W', available_coords.pop()),
            Water('W', available_coords.pop()),
            Fire('F', available_coords.pop()),
            Fire('F', available_coords.pop()),
            Fire('F', available_coords.pop()),
            Fire('F', available_coords.pop())
        ]
        return sprites
    
    def start(self):
        print('World start!')

        while self.sprites:
            world_dict = {sprite.coord: sprite for sprite in self.sprites} 

            for sprite in world_dict.values():
                print(sprite)

            enter_value = input("Please enter x1 and x2: ").split()

            if len(enter_value) != 2:
                print("Invalid input. Please enter two numbers.")
                continue

            try:
                x1, x2 = map(int, enter_value)
            except ValueError:
                print("Invalid input. Please input integers.")
                continue

            if not (0 <= x1 < self.length and 0 <= x2 < self.length):
                 print("Invalid input. Please enter available coords.")
                 continue
            
            if x1 == x2:
                print("Invalid input. Coordinates must be different.")
                continue

            if x1 in world_dict and x2 not in world_dict:
                world_dict[x1].move(x2)
            elif x1 in world_dict and x2 in world_dict:
                self.sprites = self.handleCollision(world_dict[x1], world_dict[x2])
            
            print('--------------------------------------------------------')

    def handleCollision(self, sprite1: Sprite, sprite2: Sprite) -> List[Sprite]:
        return self.collision_handler.handleCollision(sprite1, sprite2, self.sprites)
