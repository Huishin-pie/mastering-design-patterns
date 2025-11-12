from state.state import State
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role


class StatePoisoned(State):

    def __init__(self):
        super().__init__()
    
    def __str__(self):
        return "中毒"

    def before_select_action(self, role: 'Role'):
        role.take_damage(30)
        if not role.is_alive():
            self.log.role_dead(role)