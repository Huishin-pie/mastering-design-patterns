import random
from typing import TYPE_CHECKING

from map_object.role import Action, AttackMode, Role
from map_object.map_object import Symbol, Direction

if TYPE_CHECKING:
    from map.map import Map

class Character(Role):
    SYMBOL_MAP = {
        Direction.UP: Symbol.UP,
        Direction.DOWN: Symbol.DOWN,
        Direction.LEFT: Symbol.LEFT,
        Direction.RIGHT: Symbol.RIGHT
    }
    FULL_HP = 300
    FULL_ATTACK_POWER = 1
    
    def __init__(self, name, map: "Map"):
        direction = random.choice(list(self.SYMBOL_MAP.keys()))
        symbol = self.SYMBOL_MAP[direction]
        attack_range = max(map.width, map.height)
        super().__init__(name, self.FULL_HP, self.FULL_ATTACK_POWER, attack_range, symbol, self.FULL_HP, self.FULL_ATTACK_POWER, map)
        self.current_direction = direction

    def take_turn(self):
        self.state.reduce_state_rounds()

        self.state.before_take_turn()

        if not self.is_alive():
            print(f"{self.name} is dead!")
            return

        for _ in range(self.action_times):
            if self.available_actions == [Action.MOVE]:
                self.move()

            elif self.available_actions == [Action.ATTACK]:
                self.attack()

            else:
                attempts = 3
                while attempts > 0:
                    action = input("Move or Attack? (m/a): ")

                    if action not in ["m", "a"]:
                        print("Invalid action")
                        attempts -= 1
                        continue

                    if action == "m":
                        self.move()
                        break

                    elif action == "a":
                        self.attack()
                        break

        self.state.switch_state()

    def attack(self):
        from map_object.monster import Monster
        
        objs = []
        attack_power = self.attack_power

        if self.attack_mode == AttackMode.ALL:
            objs = self.map.get_monsters()

        elif self.attack_mode == AttackMode.LINEAR:
            objs = [
                obj for obj in self.map.get_objects_in_range(self.position, self.attack_range, [self.current_direction])
                if isinstance(obj, Monster)
            ]
            
        if not objs:
            return

        for obj in objs:
            obj.damage(attack_power)

            if not obj.is_alive():
                self.map.remove_object(obj.position.x, obj.position.y)
                print(f"{obj.name} is dead!")

    def move(self):
        move_attempts = 3
        while move_attempts > 0:
            dir_str_list = [dir_enum.value[0] for dir_enum in self.can_move_directions]
            direction = input(f"Direction ({'/'.join(dir_str_list)}): ").lower()

            if direction not in dir_str_list:
                print("Invalid direction")
                move_attempts -= 1
                continue
            
            self.current_direction = Direction(direction)
            self.symbol = self.SYMBOL_MAP[self.current_direction]
            if not self.map.move_object(self, self.current_direction.value):
                print("Move failed, try again")
                move_attempts -= 1
                continue

            print(f"{self.name} moves to ({self.position.x}, {self.position.y})")

            return
        

    
    

    