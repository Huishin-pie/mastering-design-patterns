from observer.observer import Observer
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role


class ObserverCurse(Observer):

    def __init__(self, observer_role: 'Role'):
        super().__init__(observer_role)

    def on_death(self, dead_role: 'Role') -> None:
        if self.role.is_alive():
            self.role.heal(dead_role.mp)
         