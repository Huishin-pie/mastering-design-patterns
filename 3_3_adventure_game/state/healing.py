from state.state import State
from map_object.role import Role
from map_object.character import Character
from state.normal import Normal
from state.invincible import Invincible

class Healing(State):
    def __init__(self, role: Role):
        super().__init__(role, 5)

    def __str__(self):
        return f"State: Healing, State rounds: {self.state_rounds}"

    def before_take_turn(self):
        self.role.heal(30)
        print(f"{self.role.name} is healing, HP: {self.role.hp}")
        
        if self.role.hp == self.role.full_hp:
            new_state = Normal(self.role)
            self.role.change_state(new_state)

    def after_take_damage(self):
        if isinstance(self.role, Character):
            new_state = Invincible(self.role)
            self.role.change_state(new_state)

    def switch_state(self):
        if self.state_rounds == 0:
            new_state = Normal(self.role)
            self.role.change_state(new_state)
            