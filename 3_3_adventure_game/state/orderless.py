import random

from map_object.map_object import Direction
from state.state import State
from state.invincible import Invincible
from state.normal import Normal
from map_object.role import Action, Role
from map_object.character import Character

class Orderless(State):
    def __init__(self, role: Role):
        super().__init__(role, 3)

    def __str__(self):
        return f"State: Orderless, State rounds: {self.state_rounds}"

    def before_take_turn(self):
        pass

    def after_take_damage(self):
        if isinstance(self.role, Character):
            new_state = Invincible(self.role)
            self.role.change_state(new_state)

    def switch_state(self):
        if self.state_rounds == 0:
            new_state = Normal(self.role)
            self.role.change_state(new_state)

    def enter(self):
        directions = [Direction.UP, Direction.DOWN] if random.choice([True, False]) else [Direction.LEFT, Direction.RIGHT]
        self.role.can_move_directions = directions
        self.role.available_actions = [Action.MOVE]

    def exit(self):
        self.role.can_move_directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        self.role.available_actions = [Action.MOVE, Action.ATTACK]