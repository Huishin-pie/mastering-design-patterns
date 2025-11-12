from typing import TYPE_CHECKING
from state.state import State

if TYPE_CHECKING:
    from role.role import Role


class StateNormal(State):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "正常"

    def reduce_state_round(self, role: 'Role') -> None:
        pass