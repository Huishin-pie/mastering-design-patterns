from state.state import State
from map_object.role import Role
from state.normal import Normal

class Accelerated(State):
    def __init__(self, role: Role):
        super().__init__(role, 3)

    def __str__(self):
        return f"State: Accelerated, State rounds: {self.state_rounds}"

    def before_take_turn(self):
        pass

    def after_take_damage(self):
        new_state = Normal(self.role)
        self.role.change_state(new_state)

    def switch_state(self):
        if self.state_rounds == 0:
            new_state = Normal(self.role)
            self.role.change_state(new_state)

    def enter(self):
        self.role.action_times = 2

    def exit(self):
        self.role.action_times = 1
        
    
