from enum import Enum
import re


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Individual:

    def __init__(self, id: int, gender: Gender, age: int, intro: str, habit: str, coord: str):
        self.id = id
        self.gender = gender 
        self.age = age
        self.intro = intro
        self.habit = habit
        self.coord = coord


    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: int):
        if value <= 0:
            raise ValueError("ID must be greater than 0.")
        self._id = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 18:
            raise ValueError("Age must be at least 18")
        self._age = value

    @property
    def intro(self):
        return self._intro

    @intro.setter
    def intro(self, value: str):
        if not (0 <= len(value) <= 200):
            raise ValueError("Intro must be between 0 and 200 characters.")
        self._intro = value

    @property
    def habit(self):
        return self._habit

    @habit.setter
    def habit(self, value: str):
        hobbies = value.split(",")
        for hobby in hobbies:
            if not (1 <= len(hobby.strip()) <= 10):
                raise ValueError("Each hobby must be between 1 and 10 characters.")
        self._habit = value

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, value: str):
        pattern = r"^([-+]?\d*\.?\d+),\s*([-+]?\d*\.?\d+)$"
        match = re.match(pattern, value)
        if not match:
            raise ValueError("Coord must be in the format 'x,y', where x and y are numbers.")
        self._coord = value.strip()