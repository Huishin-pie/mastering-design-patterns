from typing import TYPE_CHECKING
from state.state import State

if TYPE_CHECKING:
    from role.role import Role


class StateCheerUp(State):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "鼓舞"

    def enter_state(self, role: 'Role') -> None:
        role.extra_str += 50

    def exit_state(self, role: 'Role') -> None:
        role.extra_str -= 50
