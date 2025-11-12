from typing import List, TYPE_CHECKING
from observer.observer_curse import ObserverCurse
from role.role import Role
from skill.skill import Skill, TargetSelection

if TYPE_CHECKING:
    from role.role import Role


class SkillCurse(Skill):
    MP_COST = 100

    def __init__(self):
        super().__init__(mp_cost=self.MP_COST)

    def __str__(self):
        return "詛咒"

    def action(self, role: 'Role', targets: List['Role']) -> None:
        self.log.use_skill(role, self, targets)
        for target in targets:
            target.register_observer(ObserverCurse(role))

    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        alives = self._get_alives(enemy)
        if len(alives) == 0:
            return []
        return [TargetSelection(targets=alives, amount=1)]