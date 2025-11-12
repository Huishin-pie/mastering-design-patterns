from typing import List, TYPE_CHECKING
from skill.one_punch_action.one_punch_action import OnePunchAction
from skill.skill import Skill, TargetSelection

if TYPE_CHECKING:
    from role.role import Role

class SkillOnePunch(Skill):
    MP_COST = 180

    def __init__(self, one_punch_action: OnePunchAction):
        self.one_punch_action = one_punch_action
        super().__init__(mp_cost=self.MP_COST)

    def __str__(self):
        return "一拳攻擊"

    def action(self, role: 'Role', targets: List['Role']) -> None:
        self.log.use_skill(role, self, targets)
        if targets[0].hp >= 500:
            damage_amount = 300 + role.extra_str
            self._apply_damage(role, targets, damage_amount)
        else:
            self.one_punch_action.action(role, targets[0])

    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        alives = self._get_alives(enemy)
        if len(alives) == 0:
            return []
        return [TargetSelection(targets=alives, amount=1)]