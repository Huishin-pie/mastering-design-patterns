from .sprite import Sprite


class Hero(Sprite):

    def __init__(self, display: str, coord: int):
        super().__init__(display, coord)
        self.hp = 30
    
    def __str__(self):
        return f'name: {self.display}, coord: {self.coord}, hp: {self.hp}'
    

    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        if value < 0:
            raise ValueError(f"The hp must be greater than 0.")
        self._hp = value  