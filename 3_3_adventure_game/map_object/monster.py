import random
from typing import TYPE_CHECKING, Optional

from map_object.map_object import Direction, Symbol
from map_object.role import Role, State

if TYPE_CHECKING:
    from map.map import Map

class Monster(Role):
    FULL_HP = 1
    ATTACK_POWER = 50
    ATTACK_RANGE = 1

    def __init__(self, order):
        super().__init__(self.FULL_HP, self.ATTACK_POWER, self.ATTACK_RANGE, Symbol.MONSTER)
        self.order = order

    def take_turn(self, map: "Map"):
        #todo 每回合開始時失去15點生命值
        if self.state == State.POISONED:
            self.take_damage(15)
            print(f"Monster is poisoned, HP: {self.HP}")
            if not self.is_alive():
                map.remove_object(self.position.x, self.position.y)
                print(f"Monster_{self.order} is dead!")
                return
            
        #todo 每回合開始時恢復30點生命值，直到滿血。若滿血則立刻恢復至正常狀態
        if self.state == State.HEALING:
            self.heal(30)
            print(f"Monster is healing, HP: {self.HP}")
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
            
            #todo 角色的攻擊範圍擴充至「全地圖」，且攻擊行為變成「全場攻擊」：每一次攻擊時都會攻擊到地圖中所有其餘角色，且攻擊力為50。三回合過後取得瞬身狀態。
            if self.state == State.ERUPTING:
                self.attack(map)
                print(f"Monster_{self.order} attacks all characters!")
                continue

            if self.attack(map):
                character = map.get_character()
                if character and not character.is_alive():
                    map.remove_object(character.position.x, character.position.y)
                    print("Character is dead!")
                    return
            else:
                self.move(map, None)

        #todo 狀態處理
        if self.state != State.NORMAL:
            self.state_time -= 1

        #todo 兩回合後進入爆發狀態，若在期間遭受攻擊則立刻恢復至正常狀態
        if self.state == State.STOCKPILE and self.state_time == 0:
            self.change_state(State.ERUPTING, 2)

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
            
    def attack(self, map: "Map") -> bool:
        from map_object.character import Character

        objs = []
        attack_power = self.attack_power

        #todo 角色的攻擊範圍擴充至「全地圖」，且攻擊行為變成「全場攻擊」：每一次攻擊時都會攻擊到地圖中所有其餘角色，且攻擊力為50。三回合過後取得瞬身狀態。
        if self.state == State.ERUPTING:
            attack_power = 50
            objs = [obj for obj in map.get_monsters() if obj != self] + [map.get_character()]

        else:
            objs = [
                obj for obj in map.get_objects_in_range(self.position, self.attack_range, list(Direction))
                if isinstance(obj, Character)
            ]
        
        if not objs:
            return False

        for obj in objs:
            obj.take_damage(attack_power)
            print(f"Monster_{self.order} attacks: {obj}")
            if not obj.is_alive():
                map.remove_object(obj.position.x, obj.position.y)
                print("Character is dead!")

        return True

    def take_damage(self, damage):
        #todo 無敵狀態下不受傷害
        if self.state == State.INVINCIBLE:
            return
        
        super().take_damage(damage)

        #todo 每回合中可以進行「兩次動作」，若在期間遭受攻擊則立刻恢復至正常狀態
        if self.state == State.ACCELERATED:
            self.change_state(State.NORMAL, None)

        #todo 兩回合後進入爆發狀態，若在期間遭受攻擊則立刻恢復至正常狀態
        if self.state == State.STOCKPILE:
            self.change_state(State.NORMAL, None)

    def move(self, map: "Map", directions: Optional[list[Direction]]) -> None:
        if directions is None:
            directions = list(Direction)

        random.shuffle(directions)
        for direction in directions:
            if map.move_object(self, direction.value):
                print(f"Monster_{self.order} moves to {self.position.x}, {self.position.y}")
                return
        
        print(f"Monster_{self.order} at ({self.position.x}, {self.position.y}) is trapped!")

        
    