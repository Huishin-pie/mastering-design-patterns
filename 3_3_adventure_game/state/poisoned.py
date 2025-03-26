from state.state import State
from state.normal import Normal
from map_object.role import Role
from state.invincible import Invincible
from map_object.character import Character

class Poisoned(State):
    def __init__(self, role: Role):
        super().__init__(role, 3)

    def __str__(self):
        return f"State: Poisoned, State rounds: {self.state_rounds}"

    def before_take_turn(self):
        self.role.hp -= 15
        print(f"{self.role.name} is poisoned, HP: {self.role.hp}")

    def after_take_damage(self):
        if isinstance(self.role, Character):
            new_state = Invincible(self.role)
            self.role.change_state(new_state)

    def switch_state(self):
        if self.state_rounds == 0:
            new_state = Normal(self.role)
            self.role.change_state(new_state)

    
 