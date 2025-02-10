class Sprite():

    def __init__(self, display: str, coord: int):
        self.display = display
        self.coord = coord

    def __str__(self):
        return f'name: {self.display}, coord: {self.coord}'
    

    @property
    def coord(self):
        return self._coord
    
    @coord.setter
    def coord(self, value):
        if value < 0 or value > 29:
            raise ValueError("The coord must be between 0 and 29.")
        self._coord = value  

    def move(self, index: int):
        self.coord = index