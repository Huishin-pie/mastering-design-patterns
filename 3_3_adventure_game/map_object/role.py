from abc import abstractmethod
from enum import Enum
import random
from typing import TYPE_CHECKING, List

from map_object.map_object import Direction, MapObject, Symbol
from state.normal import Normal
from state.state import State

if TYPE_CHECKING:
    from map.map import Map

class Action(Enum):
    MOVE = "move"
    ATTACK = "attack"

class AttackMode(Enum):
    LINEAR = "linear"
    ALL = "all"

class Role(MapObject):
    def __init__(self, name: str, hp: int, attack_power: int, attack_range: int, symbol: Symbol, full_hp: int, full_attack_power: int, map: "Map"):
        super().__init__(symbol, map)
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.full_hp = full_hp
        self.full_attack_power = full_attack_power
        self.state = Normal(self)
        self.action_times: int = 1
        self.can_be_attacked: bool = True
        self.can_move_directions: List[Direction] = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        self.available_actions: List[Action] = [Action.ATTACK, Action.MOVE]
        self.attack_mode: str = AttackMode.LINEAR

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            value = 0
        self._hp = value

    @abstractmethod
    def take_turn(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def damage(self, damage: int):
        if self.can_be_attacked:
            self.hp -= damage

        self.state.after_take_damage()

    def heal(self, heal: int):
        self.hp += heal
        if self.hp > self.full_hp:
            self.hp = self.full_hp
    
    def change_state(self, state: State):
        self.state.exit()
        self.state = state
        self.state.enter()

    def is_alive(self) -> bool:
        return self.hp > 0
    
    def ramdom_move(self):
        empty_positions = self.map.get_empty_positions()
        if empty_positions:
            new_position = random.choice(empty_positions)
            self.map.move_object(self, new_position)
            print(f"{self.name} moves to {new_position.x}, {new_position.y} randomly")
        
