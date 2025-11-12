from __future__ import annotations
from typing import List, TYPE_CHECKING, Optional
from abc import ABC, abstractmethod
from skill.skill_basic import SkillBasic
from state.state_normal import StateNormal

if TYPE_CHECKING:
    from observer.observer import Observer
    from skill.skill import Skill, TargetSelection
    from state.state import State
    from troop.troop import Troop


class Role(ABC):

    def __init__(self, hp: int, mp: int, str: int, name: str, state: 'State' = None, skills: Optional[List['Skill']] = None):
        self.hp = hp
        self.mp = mp
        self.str = str
        self.extra_str: int = 0
        self.name = name
        self.observers: List['Observer'] = []
        self.state = state if state is not None else StateNormal()
        base_skills: List['Skill'] = [] if skills is None else list(skills)
        base_skills.insert(0, SkillBasic())
        self.skills = base_skills
        self.troop: 'Troop' = None
        self.actionable: bool = True

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, MP: {self.mp}, STR: {self.str}, State: {self.state})"

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            raise ValueError("HP must be positive.")
        self._hp = value

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        if value < 0:
            raise ValueError("MP must be positive.")
        self._mp = value

    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, value):
        if value < 0:
            raise ValueError("Strength must be positive.")
        self._str = value

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)

        if not self.is_alive():
            for observer in self.observers:
                observer.on_death(self)

    def heal(self, amount: int) -> None:
        if amount <= 0 or not self.is_alive():
            return
        self.hp += amount

    def spend_mp(self, amount: int) -> bool:
        if amount <= 0:
            return True
        if self.mp >= amount:
            self.mp -= amount
            return True
        return False

    @abstractmethod
    def select_action(self) -> 'Skill':
        pass

    @abstractmethod
    def select_targets(self, target_selections: List['TargetSelection']) -> List['Role']:
        pass

    def execute_action(self, skill: 'Skill', targets: List['Role']) -> None:
        skill.action(self, targets)

    def before_select_action(self) -> None:
        self.state.before_select_action(self)

    def change_state(self, state: 'State') -> None:
        self.state.exit_state(self)
        self.state = state
        self.state.enter_state(self)

    def register_observer(self, observer: 'Observer') -> None:
        self.observers.append(observer)

    def unregister_observer(self, observer: 'Observer') -> None:
        self.observers.remove(observer)