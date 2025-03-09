from application.tank import Tank
from command.command import Command


class MoveBackward(Command):

    def __init__(self, tank: Tank):
        super().__init__()
        self.tank = tank

    def __str__(self):
        return "MoveTankBackward" 

    def execute(self):
        self.tank.move_backward()

    def undo(self):
        self.tank.move_forward()

    