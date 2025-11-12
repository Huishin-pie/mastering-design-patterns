from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role
    from skill.skill import Skill, TargetSelection


class AIStrategy(ABC):

    @abstractmethod
    def select_action(self, skills: List['Skill']) -> 'Skill':
        pass

    @abstractmethod
    def select_targets(self, target_selections: List['TargetSelection']) -> List['Role']:
        pass