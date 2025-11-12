from typing import List, TYPE_CHECKING
from role.role import Role

if TYPE_CHECKING:
    from skill.skill import Skill, TargetSelection
    from state.state import State


class Hero(Role):

    def __init__(self, hp: int, mp: int, str: int, state: 'State', skills: List['Skill']):
        super().__init__(hp, mp, str, "Hero", state, skills)

    def select_action(self) -> 'Skill':
        while True:
            action = input(f"選擇行動：{' '.join(f'({i}) {skill}' for i, skill in enumerate(self.skills))}")

            if action not in [str(i) for i in range(len(self.skills))]:
                print("Invalid action")
                continue

            return self.skills[int(action)]

    def select_targets(self, target_selections: List['TargetSelection']) -> List['Role']:
        if not target_selections:
            return []
        
        all_targets = []
        for selection in target_selections:
            if len(selection.targets) <= selection.amount:
                all_targets.extend(selection.targets)
                continue

            while True:
                action = input(f"選擇 {selection.amount} 位目標：{' '.join(f'({i}) [{target.troop.id}]{target.name}' for i, target in enumerate(selection.targets))}")
                
                try:
                    indices = [int(x.strip()) for x in action.split(',')]
                    
                    if len(set(indices)) != len(indices):
                        print("不能選擇重複的目標")
                        continue
                    
                    if len(indices) != selection.amount or any(i < 0 or i >= len(selection.targets) for i in indices):
                        print("選擇數量不正確或目標無效")
                        continue
                    
                    selected = [selection.targets[i] for i in indices]
                    all_targets.extend(selected)
                    break
                except ValueError:
                    print("無效的輸入格式")
                    continue
        
        return all_targets