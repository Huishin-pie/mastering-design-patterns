from typing import List

from command.command import Command


class Keyboard():

    def __init__(self):
        self.commands = self._create_command_dict()

    def _create_command_dict(self):
        result = {}
        keys = [
                "a", "b", "c", "d", "e", "f", "g"
                , "h", "i", "j", "k", "l", "m"
                , "n", "o", "p", "q", "r", "s"
                , "t", "u", "v", "w", "x", "y", "z"
                ]
        
        for key in keys:
            result[key]: List[Command]= [] # type: ignore

        return result

    def press(self, key: str):
        if key in self.commands and self.commands[key]:
            for command in self.commands[key]:
                command.execute()

    def set_command(self, key: str, commands: List[Command]):
        if key in self.commands:
            self.commands[key] = commands
        else:
            raise ValueError(f"Button {key} not supported.")
        
    def get_command(self, key: str):
        return self.commands[key]
        
    def reset(self):
        print("Reset keyboard.")
        self.commands = self._create_command_dict()