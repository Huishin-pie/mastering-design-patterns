from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from role.role import Role


class Troop():

    def __init__(self, id: int, members: List['Role'] = None):
        self.id = id
        self.members = members

    @property
    def members(self) -> List['Role']:
        return self._members

    @members.setter
    def members(self, value: List['Role']) -> None:
        if len(value) == 0:
            raise ValueError("Troop must have at least one member.")
        self._members = value

    def is_annihilated(self) -> bool:
        return all(not member.is_alive() for member in self.members)

    def get_members(self, is_alive: bool = False) -> List['Role']:
        if is_alive:
            return [member for member in self.members if member.is_alive()]
        return [member for member in self.members]

    def get_ally(self, role: 'Role') -> List['Role']:
        return [member for member in self.members if member.is_alive() and member != role]

    def get_hero(self) -> 'Role':
        for member in self.members:
            if member.__class__.__name__ == "Hero":
                return member
        return None

    def add_member(self, role: 'Role') -> None:
        self.members.append(role)
        role.troop = self
