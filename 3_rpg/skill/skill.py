from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, TYPE_CHECKING
from log.log import Log

if TYPE_CHECKING:
    from role.role import Role


@dataclass
class TargetSelection:
    targets: List['Role']
    amount: int

class Skill(ABC):

    def __init__(self, mp_cost: int):
        self.mp_cost = mp_cost
        self.log = Log()

    @abstractmethod
    def action(self, role: 'Role', targets: List['Role']) -> None:
        pass
    
    @abstractmethod
    def get_target_selections(self, role: 'Role', ally: List['Role'], enemy: List['Role']) -> List[TargetSelection]:
        pass
    
    def get_mp_cost(self) -> int:
        return self.mp_cost

    def _get_alives(self, roles: List['Role']) -> List['Role']:
        return [r for r in roles if r.is_alive()]

    def _apply_damage(self, attacker: 'Role', targets: List['Role'], amount: int) -> None:
        for target in targets:
            target.take_damage(amount)
            self.log.take_damage(attacker, target, amount)
            if not target.is_alive():
                self.log.role_dead(target)