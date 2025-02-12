from typing import List, Union

from .player import Player
from card.card import Card


class HumanPlayer(Player):

    def __init__(self, order: int):
        super().__init__(order)


    def name_self(self):
        while True:
            name = input("請輸入你的名字: ").strip()
            if self._is_valid(name):
                self.name = name
                return
            else:
                print("輸入只能包含字母 (A-Z, a-z)、數字 (0-9) 和中文字")
                continue

    def play_or_pass(self) -> Union[List[Card], None]:
        while True:
            input_value = input("請輸入序號: ")

            if input_value == "-1":
                return None

            try:
                index_list = [int(index) for index in input_value.split()]

                if not index_list:
                    print("輸入不能為空，請重新輸入")
                    continue

                cards = []
                for index in index_list:
                    if 0 <= index < len(self.hand_cards):
                        cards.append(self.hand_cards[index])
                    else:
                        print(f"無效的索引: {index}，請重新輸入")
                        break
                else:
                    return cards

            except ValueError:
                print("無效的輸入，請確保輸入的是有效的數字序號")