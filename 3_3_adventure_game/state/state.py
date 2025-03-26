from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from map_object.role import Role

class State(ABC):
    def __init__(self, role: "Role", state_rounds: int):
        self.role = role
        self.state_rounds = state_rounds

    @abstractmethod
    def before_take_turn(self):
        pass

    @abstractmethod
    def after_take_damage(self):
        pass
    
    @abstractmethod
    def switch_state(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def reduce_state_rounds(self):
        from state.normal import Normal

        if not isinstance(self, Normal):
            self.state_rounds -= 1
