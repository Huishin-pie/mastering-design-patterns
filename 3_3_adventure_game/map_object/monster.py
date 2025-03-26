import random
from typing import TYPE_CHECKING

from map_object.map_object import Direction, Symbol
from map_object.role import Action, AttackMode, Role

if TYPE_CHECKING:
    from map.map import Map

class Monster(Role):
    FULL_HP = 1
    FULL_ATTACK_POWER = 50
    ATTACK_RANGE = 1

    def __init__(self, name, map: "Map"):
        super().__init__(name, self.FULL_HP, self.FULL_ATTACK_POWER, self.ATTACK_RANGE, Symbol.MONSTER, self.FULL_HP, self.FULL_ATTACK_POWER, map)

    def take_turn(self):
        self.state.reduce_state_rounds()

        self.state.before_take_turn()
        
        if not self.is_alive():
            self.map.remove_object(self.position.x, self.position.y)
            print(f"{self.name} is dead!")
            return

        for _ in range(self.action_times):
            if self.available_actions == [Action.MOVE]:
                self.move()
                continue

            elif self.available_actions == [Action.ATTACK]:
                self.attack()
                continue

            if self.attack():
                character = self.map.get_character()
                if character and not character.is_alive():
                    self.map.remove_object(character.position.x, character.position.y)
                    print(f"{character.name} is dead!")
                    return
            else:
                self.move()

        self.state.switch_state()
            
    def attack(self) -> bool:
        from map_object.character import Character

        objs = []

        if self.attack_mode == AttackMode.ALL:
            objs = [obj for obj in self.map.get_monsters() if obj != self] + [self.map.get_character()]

        elif self.attack_mode == AttackMode.LINEAR:
            objs = [
                obj for obj in self.map.get_objects_in_range(self.position, self.attack_range, list(Direction))
                if isinstance(obj, Character)
            ]
        
        if not objs:
            return False

        for obj in objs:
            obj.damage(self.attack_power)
            print(f"{self.name} attacks {obj.name}")

            if not obj.is_alive():
                self.map.remove_object(obj.position.x, obj.position.y)
                print(f"{obj.name} is dead!")

        return True
    
    def move(self) -> None:
        random.shuffle(self.can_move_directions)
        for direction in self.can_move_directions:
            if self.map.move_object(self, direction.value):
                print(f"{self.name} moves to {self.position.x}, {self.position.y}")
                return
        
        print(f"{self.name} at ({self.position.x}, {self.position.y}) is trapped!")

        
    