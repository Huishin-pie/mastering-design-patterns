from typing import List

from application.tank import Tank
from application.telecom import Telecom
from command.command import Command
from command.connect import Connect
from command.disconnect import Disconnect
from command.move_backward import MoveBackward
from command.move_forward import MoveForward
from command.reset import Reset
from main_controller.keyboard import Keyboard


class MainController():

    def __init__(self):
        self.keyboard = Keyboard()
        self.s1: List[List[Command]] = []
        self.s2: List[List[Command]] = []

    def start(self):
        tank = Tank()
        telecom = Telecom()

        command_list = [
            Connect(telecom), Disconnect(telecom),
            MoveForward(tank), MoveBackward(tank),
            Reset(self.keyboard)
        ]

        while True:
            try:
                input_val = input("(1) 快捷鍵設置 (2) Undo (3) Redo (字母) 按下按鍵:").strip()

                if input_val.isalpha():
                    self.keyboard.press(input_val)
                    commands = self.keyboard.get_command(input_val)
                    if commands:
                        self.s1.append(commands)
                        self.s2.clear()

                elif int(input_val) == 1:
                    while True:
                        set_macro = input("設置巨集指令 (y/n)：").strip().lower()
                        if set_macro in {"y", "n"}:
                            break
                        print("輸入錯誤，請輸入 'y' 或 'n'")

                    key = input("key: ").strip()

                    if set_macro == "y":
                        print(f"要將哪些指令設置成快捷鍵 {key} 的巨集（輸入多個數字，以空白隔開）: ")
                    else: 
                        print(f"要將哪一道指令設置到快捷鍵 {key} 上: ")

                    print("\n".join(f"{i}: {c}" for i, c in enumerate(command_list)))

                    while True:
                        try:
                            if set_macro == "y":
                                commands = [command_list[int(val)] for val in input().split()]
                            else:
                                command_val = int(input())
                                commands = [command_list[command_val]]

                            self.set_command(key, commands)
                            break
                        except (ValueError, IndexError):
                            print("輸入錯誤，請輸入有效的數字")

                elif int(input_val) == 2:
                    self.undo()

                elif int(input_val) == 3:
                    self.redo()

                else:
                    print("輸入錯誤，請輸入 1、2、3 或快捷鍵")

            except Exception as e:
                print(f"發生錯誤: {e}，請再試一次")

    def set_command(self, key: str, commands: List[Command]):
        self.keyboard.set_command(key, commands)

    def undo(self):
        if self.s1:
            commands = self.s1.pop()
            for command in reversed(commands):
                command.undo()
            self.s2.append(commands)

    def redo(self):
        if self.s2:
            commands = self.s2.pop()
            for command in commands:
                command.execute()
            self.s1.append(commands)