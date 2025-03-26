from map_object.character import Character
from state.invincible import Invincible
from state.state import State
from map_object.role import AttackMode, Role
from state.teleport import Teleport

class Erupting(State):
    def __init__(self, role: Role):
        super().__init__(role, 3)

    def __str__(self):
        return f"State: Erupting, State rounds: {self.state_rounds}"

    def before_take_turn(self):
        pass

    def after_take_damage(self):
        if isinstance(self.role, Character):
            new_state = Invincible(self.role)
            self.role.change_state(new_state)

    def switch_state(self):
        if self.state_rounds == 0:
            new_state = Teleport(self.role)
            self.role.change_state(new_state)

    def enter(self):
        self.role.attack_power = 50
        self.role.attack_mode = AttackMode.ALL

    def exit(self):
        self.role.attack_power = self.role.full_attack_power
        self.role.attack_mode = AttackMode.LINEAR