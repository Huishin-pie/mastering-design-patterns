from skill.one_punch_action.one_punch_action import OnePunchAction
from state.state_normal import StateNormal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role


class OnePunchNormal(OnePunchAction):
    
    def __init__(self, next: 'OnePunchAction' = None):
        super().__init__(next)

    def match(self, role: 'Role') -> bool:
        if isinstance(role.state, StateNormal):
            return True
        return False

    def do_action(self, role: 'Role', target: 'Role') -> None:
        damage_amount = 100 + role.extra_str

        target.take_damage(damage_amount)
        self.log.take_damage(role, target, damage_amount)
        if not target.is_alive():
            self.log.role_dead(target)
