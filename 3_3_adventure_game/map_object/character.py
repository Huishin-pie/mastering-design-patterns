import random
from typing import List, TYPE_CHECKING

from map_object.role import Role, State
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
    ATTACK_POWER = 1
    
    def __init__(self, attack_range):
        direction = random.choice(list(Direction))
        symbol = self.SYMBOL_MAP[direction]
        super().__init__(self.FULL_HP, self.ATTACK_POWER, attack_range, symbol)
        self.direction = direction

    def take_turn(self, map: "Map"):
        #todo 每回合開始時失去15點生命值
        if self.state == State.POISONED:
            self.take_damage(15)
            print(f"Character is poisoned, HP: {self.HP}")
            if not self.is_alive():
                print("Character is dead!")
                return
        
        #todo 每回合開始時恢復30點生命值，直到滿血。若滿血則立刻恢復至正常狀態
        if self.state == State.HEALING:
            self.heal(30)
            print(f"Character is healing, HP: {self.HP}")
            if self.HP == self.FULL_HP:
                self.change_state(State.NORMAL, None)

        #todo 每回合中可以進行「兩次動作」，若在期間遭受攻擊則立刻恢復至正常狀態
        action_times = 1
        if self.state == State.ACCELERATED:
            action_times = 2

        for _ in range(action_times):
            #todo 每回合隨機取得以下其中一種效果：1. 只能進行上下移動 2. 只能進行左右移動（角色只能移動，不能選擇做其他操作）
            if self.state == State.ORDERLESS:
                directions = [Direction.UP, Direction.DOWN] if random.choice([True, False]) else [Direction.LEFT, Direction.RIGHT]
                self.move(map, directions)
                continue

            attempts = 3
            while attempts > 0:
                action = input("Move or Attack? (m/a): ")

                if action not in ["m", "a"]:
                    print("Invalid action")
                    attempts -= 1
                    continue

                if action == "m":
                    self.move(map)
                    break

                elif action == "a":
                    self.attack(map)
                    break

        #todo 狀態處理
        if self.state != State.NORMAL:
            self.state_time -= 1

        #todo 兩回合後進入爆發狀態，若在期間遭受攻擊則立刻恢復至正常狀態
        if self.state == State.STOCKPILE and self.state_time == 0:
            self.change_state(State.ERUPTING, 2)

        #todo 角色的攻擊範圍擴充至「全地圖」，且攻擊行為變成「全場攻擊」：每一次攻擊時都會攻擊到地圖中所有其餘角色，且攻擊力為50。三回合過後取得瞬身狀態。
        if self.state == State.ERUPTING and self.state_time == 0:
            self.change_state(State.TELEPORT, 3)

        #todo 一回合後角色的位置將被隨機移動至任一空地
        if self.state == State.TELEPORT:
            empty_positions = map.get_empty_positions()
            if empty_positions:
                new_position = random.choice(empty_positions)
                map.move_object(self, new_position)
                print(f"Monster_{self.order} teleports to {new_position.x}, {new_position.y}")

        #todo 狀態處理
        if self.state != State.NORMAL and self.state_time == 0:
            self.change_state(State.NORMAL, None)

    def attack(self, map: "Map"):
        from map_object.monster import Monster
        
        objs = []
        attack_power = self.attack_power

        #todo 角色的攻擊範圍擴充至「全地圖」，且攻擊行為變成「全場攻擊」：每一次攻擊時都會攻擊到地圖中所有其餘角色，且攻擊力為50。三回合過後取得瞬身狀態。
        if self.state == State.ERUPTING:
            attack_power = 50
            objs = map.get_monsters()
        else:
            objs = [
            obj for obj in map.get_objects_in_range(self.position, self.attack_range, [self.direction])
            if isinstance(obj, Monster)
        ]
            
        if not objs:
            return

        for obj in objs:
            # print(obj.position.x, obj.position.y)
            obj.take_damage(attack_power)
            if not obj.is_alive():
                map.remove_object(obj.position.x, obj.position.y)
                print(f"Monster_{obj.order} is dead!")

    def take_damage(self, damage):
        #todo 無敵狀態下不受傷害
        if self.state == State.INVINCIBLE:
            return
        
        super().take_damage(damage)
    
        #todo 主角的狀態並非「蓄力」或「加速」狀態，則會在受到傷害後立刻獲得無敵狀態
        if self.state not in [State.STOCKPILE, State.ACCELERATED, State.INVINCIBLE]:
            self.change_state(State.INVINCIBLE, 3)

        #todo 每回合中可以進行「兩次動作」，若在期間遭受攻擊則立刻恢復至正常狀態
        if self.state == State.ACCELERATED:
            self.change_state(State.NORMAL, None)
        
        #todo 兩回合後進入爆發狀態，若在期間遭受攻擊則立刻恢復至正常狀態
        if self.state == State.STOCKPILE:
            self.change_state(State.NORMAL, None)

    def move(self, map: "Map", directions: List[Direction] = list(Direction)):
        move_attempts = 3
        while move_attempts > 0:
            dir_str_list = [dir_enum.value[0] for dir_enum in directions]
            direction = input(f"Direction ({'/'.join(dir_str_list)}): ").lower()

            if direction not in dir_str_list:
                print("Invalid direction")
                move_attempts -= 1
                continue
            
            self.direction = Direction(direction)
            self.symbol = self.SYMBOL_MAP[self.direction]
            if not map.move_object(self, self.direction.value):
                print("Move failed, try again")
                move_attempts -= 1
                continue

            print(f"Character moves to ({self.position.x}, {self.position.y})")

            return
        

    
    

    