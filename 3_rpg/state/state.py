from abc import ABC
from typing import TYPE_CHECKING
from log.log import Log

if TYPE_CHECKING:
    from role.role import Role

class State(ABC):

    def __init__(self):
        self.round = 3
        self.log = Log()

    def enter_state(self, role: 'Role') -> None:
        pass

    def exit_state(self, role: 'Role') -> None:
        pass

    def before_select_action(self, role: 'Role') -> None:
        pass

    def reduce_state_round(self, role: 'Role') -> None:
        from state.state_normal import StateNormal
        
        if self.round > 0:
            self.round -= 1

        if self.round == 0:
            role.change_state(StateNormal())