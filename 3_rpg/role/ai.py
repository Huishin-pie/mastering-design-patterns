from typing import List, TYPE_CHECKING
from role.role import Role

if TYPE_CHECKING:
    from skill.skill import Skill, TargetSelection
    from state.state import State
    from role.ai_strategy.ai_strategy import AIStrategy


class AI(Role):

    def __init__(self, hp: int, mp: int, str: int, name: str, state: 'State', skills: List['Skill'], strategy: 'AIStrategy'):
        self.strategy = strategy
        super().__init__(hp, mp, str, name, state, skills)

    def select_action(self) -> 'Skill':
        print(f"選擇行動：{' '.join(f'({i}) {skill}' for i, skill in enumerate(self.skills))}")
        return self.strategy.select_action(self.skills)

    def select_targets(self, target_selections: List['TargetSelection']) -> List['Role']:
        return self.strategy.select_targets(target_selections)