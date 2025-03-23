from map.map import Map

class Game:
    def __init__(self, map_width, map_height):
        self.map = Map(map_width, map_height)
        self.round = 1

    def start(self):
        print("Game start!")

        while not self.game_end():
            self.play_round()
            self.round += 1

        print("Game over!")

    def play_round(self):
        character = self.map.get_character()

        print(f"Round: {self.round}")
        print(self.map)
        print(f"Character - State: {character.state}, State time: {character.state_time}, HP: {character.HP}")

        character.take_turn(self.map)
        if self.game_end():
            return

        monsters = self.map.get_monsters()
        for monster in monsters:
            print(f"Monster {monster.order} - State: {monster.state}, State time: {monster.state_time}, HP: {monster.HP}")
            monster.take_turn(self.map)
            if self.game_end():
                return

    def game_end(self) -> bool:
        return not self.map.monsters_alive() or not self.map.get_character()