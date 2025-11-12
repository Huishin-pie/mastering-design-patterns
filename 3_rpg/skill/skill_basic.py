from typing import List, TYPE_CHECKING
from skill.skill import Skill, TargetSelection

if TYPE_CHECKING:
    from role.role import Role


class SkillBasic(Skill):
    MP_COST = 0

    def __init__(self):
        super().__init__(mp_cost=self.MP_COST)

    def __str__(self):
        return "普通攻擊"

    def action(self, role: 'Role', targets: List['Role']) -> None:
        self.log.basic_attack(role, targets)
        damage_amount = role.str + role.extra_str
        self._apply_damage(role, targets, damage_amount)

    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        alives = self._get_alives(enemy)
        if len(alives) == 0:
            return []
        return [TargetSelection(targets=alives, amount=1)]