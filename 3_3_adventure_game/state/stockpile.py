from state.normal import Normal
from state.state import State
from state.erupting import Erupting
from map_object.role import Role

class Stockpile(State):
    def __init__(self, role: Role):
        super().__init__(role, 2)

    def __str__(self):
        return f"State: Stockpile, State rounds: {self.state_rounds}"
    
    def before_take_turn(self):
        pass

    def after_take_damage(self):
        new_state = Normal(self.role)
        self.role.change_state(new_state)

    def switch_state(self):
        if self.state_rounds == 0:
            new_state = Erupting(self.role)
            self.role.change_state(new_state)
    