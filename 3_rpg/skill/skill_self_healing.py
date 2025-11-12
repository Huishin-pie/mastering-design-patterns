from typing import List, TYPE_CHECKING
from skill.skill import Skill, TargetSelection

if TYPE_CHECKING:
    from role.role import Role


class SkillSelfHealing(Skill):
    MP_COST = 50
    HEAL_AMOUNT = 150

    def __init__(self):
        super().__init__(mp_cost=self.MP_COST)

    def __str__(self):
        return "自我治療"

    def action(self, role: 'Role', targets: List['Role']) -> None:
        self.log.use_skill(role, self)
        role.heal(self.HEAL_AMOUNT)

    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        return []