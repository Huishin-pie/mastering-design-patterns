from application.tank import Tank
from command.command import Command


class MoveForward(Command):

    def __init__(self, tank: Tank):
        super().__init__()
        self.tank = tank

    def __str__(self):
        return "MoveTankForward" 

    def execute(self):
        self.tank.move_forward()

    def undo(self):
        self.tank.move_backward()