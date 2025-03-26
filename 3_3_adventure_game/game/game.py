import random

from map.map import Map

class Game:
    def __init__(self, map: Map):
        self.map = map
        self.round = 1

    def start(self):
        print("Game start!")

        while not self.game_end():
            print("----------------------------------------------")
            self.play_round()
            self.round += 1

        print("Game over!")

    def play_round(self):
        self.map.add_monsters(random.randint(0, 1))
        self.map.add_treasures(random.randint(0, 2))

        print(f"Round: {self.round}")
        print(self.map)

        character = self.map.get_character()
        if not character:
            return
        print(f"{character.name} - {character.state}, HP: {character.hp}")
        character.take_turn()
        if self.game_end():
            return

        monsters = self.map.get_monsters()
        if not monsters:
            return
        for monster in monsters:
            print(f"{monster.name} - {monster.state}, HP: {monster.hp}")
            monster.take_turn()
            if self.game_end():
                return

    def game_end(self) -> bool:
        return not self.map.get_monsters() or not self.map.get_character()