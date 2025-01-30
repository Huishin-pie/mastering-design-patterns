from .sprite import Sprite


class Water(Sprite):

    def __init__(self, display: str, coord: int):
        super().__init__(display, coord)