from typing import List, TYPE_CHECKING
from skill.skill import Skill, TargetSelection
from state.state_poisoned import StatePoisoned

if TYPE_CHECKING:
    from role.role import Role


class SkillPoison(Skill):
    MP_COST = 80

    def __init__(self):
        super().__init__(mp_cost=self.MP_COST)

    def __str__(self):
        return "下毒"

    def action(self, role: 'Role', targets: List['Role']) -> None:
        self.log.use_skill(role, self, targets)
        for target in targets:
            target.change_state(StatePoisoned())

    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        alives = self._get_alives(enemy)
        if len(alives) == 0:
            return []
        return [TargetSelection(targets=alives, amount=1)]