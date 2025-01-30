from abc import ABC, abstractmethod
from typing import List
from typing import Optional

from sprite.sprite import Sprite


class CollisionHandler(ABC):

    def __init__(self, next: Optional['CollisionHandler']):
        self.next = next

    
    def handleCollision(self, sprite1: Sprite, sprite2: Sprite, sprites: List[Sprite]) -> List[Sprite]:
        if self.match(sprite1, sprite2):
            return self.handle(sprite1, sprite2, sprites)
        elif self.next is not None:
            return self.next.handleCollision(sprite1, sprite2, sprites)

    @abstractmethod
    def match(self, sprite1: Sprite, sprite2: Sprite) -> bool:
        pass

    @abstractmethod
    def handle(self, sprite1: Sprite, sprite2: Sprite, sprites: List[Sprite]) -> List[Sprite]:
        pass