from typing import List, TYPE_CHECKING
from role.ai_strategy.ai_strategy import AIStrategy

if TYPE_CHECKING:
    from role.role import Role
    from skill.skill import Skill, TargetSelection


class StrategySeed(AIStrategy):

    def __init__(self):
        self.seed = 0

    def select_action(self, skills: List['Skill']) -> 'Skill':
        skill = skills[self.seed % len(skills)]
        self.seed += 1
        return skill

    def select_targets(self, target_selections: List['TargetSelection']) -> List['Role']:
        if not target_selections:
            return []
        
        targets = []
        for selection in target_selections:
            if len(selection.targets) <= selection.amount:
                targets.extend(selection.targets)
                continue
            
            start = self.seed % len(selection.targets)
            selected = []
            for i in range(selection.amount):
                selected.append(selection.targets[(start + i) % len(selection.targets)])
            targets.extend(selected)
            self.seed += 1
        return targets