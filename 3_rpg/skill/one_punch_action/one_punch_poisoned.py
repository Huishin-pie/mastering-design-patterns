from skill.one_punch_action.one_punch_action import OnePunchAction
from state.state_poisoned import StatePoisoned
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role


class OnePunchPoisoned(OnePunchAction):
    
    def __init__(self, next: 'OnePunchAction' = None):
        super().__init__(next)

    def match(self, role: 'Role') -> bool:
        if isinstance(role.state, StatePoisoned):
            return True
        return False

    def do_action(self, role: 'Role', target: 'Role') -> None:
        damage_times = 3
        damage_amount = 80 + role.extra_str

        for _ in range(damage_times):
            target.take_damage(damage_amount)
            self.log.take_damage(role, target, damage_amount)
            if not target.is_alive():
                self.log.role_dead(target)
                break