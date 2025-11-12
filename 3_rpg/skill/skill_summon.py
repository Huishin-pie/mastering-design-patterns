from typing import List, TYPE_CHECKING
from observer.observer_summon import ObserverSummon
from role.ai import AI
from role.ai_strategy.strategy_seed import StrategySeed
from skill.skill import Skill, TargetSelection
from state.state_normal import StateNormal

if TYPE_CHECKING:
    from role.role import Role

class SkillSummon(Skill):
    MP_COST = 150

    def __init__(self):
        super().__init__(mp_cost=self.MP_COST)

    def __str__(self):
        return "召喚"

    def action(self, role: 'Role', targets: List['Role']) -> None:
        self.log.use_skill(role, self)
        summon_role = AI(hp=100, mp=0, str=50, name="Slime", state=StateNormal(), skills=[], strategy=StrategySeed())
        summon_role.register_observer(ObserverSummon(role))
        if role.troop:
            role.troop.add_member(summon_role)

    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        return []