from typing import TYPE_CHECKING
from state.state import State

if TYPE_CHECKING:
    from role.role import Role


class StatePetrochemical(State):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "石化"

    def enter_state(self, role: 'Role') -> None:
        role.actionable = False

    def exit_state(self, role: 'Role') -> None:
        role.actionable = True