from abc import ABC, abstractmethod
from log.log import Log
from role.role import Role


class OnePunchAction(ABC):

    def __init__(self, next: 'OnePunchAction' = None):
        self.next = next
        self.log = Log()

    def action(self, role: Role, target: Role) -> None:
        if self.match(target):
            self.do_action(role, target)
        elif self.next:
            self.next.action(role, target)

    def match(self, role: Role) -> bool:
        return True

    @abstractmethod
    def do_action(self, role: Role, target: Role) -> None:
        pass
