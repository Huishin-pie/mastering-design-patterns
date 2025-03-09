from command.command import Command
from main_controller.keyboard import Keyboard


class Reset(Command):

    def __init__(self, keyboard: Keyboard):
        super().__init__()
        self.keyboard = keyboard

    def __str__(self):
        return "ResetMainControlKeyboard" 

    def execute(self):
        self.keyboard.reset()

    def undo(self):
        pass