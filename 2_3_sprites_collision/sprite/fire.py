from .sprite import Sprite


class Fire(Sprite):

    def __init__(self, display: str, coord: int):
        super().__init__(display, coord)