from typing import List, TYPE_CHECKING
from skill.skill import Skill, TargetSelection

if TYPE_CHECKING:
    from role.role import Role


class SkillWaterball(Skill):
    MP_COST = 50
    DAMAGE_AMOUNT = 120

    def __init__(self):
        super().__init__(mp_cost=self.MP_COST)

    def __str__(self):
        return "水球"

    def action(self, role: 'Role', targets: List['Role']) -> None:
        self.log.use_skill(role, self, targets)
        damage_amount = self.DAMAGE_AMOUNT + role.extra_str
        self._apply_damage(role, targets, damage_amount)

    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        alives = self._get_alives(enemy)
        if len(alives) == 0:
            return []
        return [TargetSelection(targets=alives, amount=1)]