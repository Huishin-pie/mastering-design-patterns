from state.state import State
from state.normal import Normal
from map_object.role import Role

class Invincible(State):
    def __init__(self, role: Role):
        super().__init__(role, 2)

    def __str__(self):
        return f"State: Invincible, State rounds: {self.state_rounds}"

    def before_take_turn(self):
        pass

    def after_take_damage(self):
        pass

    def switch_state(self):
        if self.state_rounds == 0:
            new_state = Normal(self.role)
            self.role.change_state(new_state)

    def enter(self):
        self.role.can_be_attacked = False

    def exit(self):
        self.role.can_be_attacked = True

