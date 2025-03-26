from typing import TYPE_CHECKING

from state.state import State

if TYPE_CHECKING:
    from map_object.role import Role

class Normal(State):
    def __init__(self, role: "Role"):
        super().__init__(role, None)
    
    def __str__(self):
        return f"State: Normal, State rounds: {self.state_rounds}"

    def before_take_turn(self):
        pass

    def after_take_damage(self):
        from map_object.character import Character
        from state.invincible import Invincible

        if isinstance(self.role, Character):
            new_state = Invincible(self.role)
            self.role.change_state(new_state)

    def switch_state(self):
        pass