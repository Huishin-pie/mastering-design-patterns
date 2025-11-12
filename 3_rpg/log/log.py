from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from skill.skill import Skill
    from role.role import Role


class Log:

    def __init__(self):
        self.entries = []

    def use_skill(self, role: 'Role', skill: 'Skill', targets: List['Role'] = []) -> None:
        if not targets:
            print(f"[{role.troop.id}]{role.name} 使用了 {skill}。")
        else:
            print(f"[{role.troop.id}]{role.name} 對 {' '.join(f'[{target.troop.id}]{target.name}' for target in targets)} 使用了 {skill}。")
    
    def basic_attack(self, role: 'Role', targets: List['Role']) -> None:
        print(f"[{role.troop.id}]{role.name} 攻擊 {' '.join(f'[{target.troop.id}]{target.name}' for target in targets)}。")

    def take_damage(self, role: 'Role', target: 'Role', amount: int) -> None:
        print(f"[{role.troop.id}]{role.name} 對 [{target.troop.id}]{target.name} 造成 {amount} 點傷害。")

    def role_dead(self, role: 'Role') -> None:
        print(f"[{role.troop.id}]{role.name} 死亡。")

    
