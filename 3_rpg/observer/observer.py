from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role


class Observer(ABC):

    def __init__(self, observer_role: 'Role'):
        self.role = observer_role

    @abstractmethod
    def on_death(self, dead_role: 'Role') -> None:
        pass