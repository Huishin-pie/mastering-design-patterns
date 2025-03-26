from typing import List
import random

from map_object.map_object import MapObject, Position, Direction
from map_object.treasure import Treasure, TreasureType
from map_object.monster import Monster
from map_object.character import Character
from map_object.obstacle import Obstacle

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid: List[List[MapObject | None]] = self._initMapObjects()

    def __str__(self):
        result = []
        for row in self.grid:
            result.append(" ".join(["." if cell is None else str(cell) for cell in row]))
        return "\n".join(result)

    def _initMapObjects(self) -> List[MapObject]:
        width, height = self.width, self.height
        self.grid: List[List[MapObject | None]] = [[None for _ in range(width)] for _ in range(height)]

        self.add_treasures(random.randint(4, 6))
        self.add_monsters(random.randint(4, 6))
        self._place_obstacles(random.randint(3, 5))
        self._place_character()

        return self.grid
    
    def _get_random_position(self) -> tuple:
        empty_positions = self.get_empty_positions()
        if not empty_positions:
            raise ValueError("No empty positions available")
        return random.choice(empty_positions)
            
    def add_treasures(self, num_treasures: int):
        if num_treasures == 0:
            return
        
        object_probabilities = {
            TreasureType.SUPER_STAR: 10,
            TreasureType.POISON: 25,
            TreasureType.ACCELERATING_POTION: 20,
            TreasureType.HEALING_POTION: 15,
            TreasureType.DEVIL_FRUIT: 10,
            TreasureType.KINGS_ROCK: 10,
            TreasureType.DOKODEMO_DOOR: 10
        }
        
        for _ in range(num_treasures):
            position = self._get_random_position()
            treasure_type = random.choices(list(object_probabilities.keys()), weights=object_probabilities.values(), k=1)[0]
            treasure = Treasure(treasure_type, self)
            treasure.position = position
            self.grid[position.y][position.x] = treasure

    def add_monsters(self, num_monsters: int):
        if num_monsters == 0:
            return
        
        num = len(self.get_monsters())
        
        for i in range(num_monsters):
            position = self._get_random_position()
            monster = Monster(f"Monster_{i + num}", self)
            monster.position = position
            self.grid[position.y][position.x] = monster

    def _place_obstacles(self, num_obstacles: int):
        for _ in range(num_obstacles):
            position = self._get_random_position()
            obstacle = Obstacle(self)
            obstacle.position = position
            self.grid[position.y][position.x] = obstacle

    def _place_character(self):
        position = self._get_random_position()
        character = Character("Character", self)
        character.position = position
        self.grid[position.y][position.x] = character

    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= y < self.height and 0 <= x < self.width

    def remove_object(self, x, y):
        if self.is_within_bounds(x, y):
            self.grid[y][x] = None
        else:
            raise ValueError("Coordinates out of bounds")

    def move_object(self, obj: MapObject, direction: str) -> bool:
        direction_map = {
            "u": (0, -1),  # 上 (y-1)
            "d": (0, 1),   # 下 (y+1)
            "l": (-1, 0),  # 左 (x-1)
            "r": (1, 0)    # 右 (x+1)
        }

        if direction not in direction_map:
            return False

        dx, dy = direction_map[direction]
        new_x = obj.position.x + dx
        new_y = obj.position.y + dy

        if not self.is_within_bounds(new_x, new_y):
            return False
        
        target_obj = self.grid[new_y][new_x]
        current_obj = self.grid[obj.position.y][obj.position.x]

        if target_obj:
            if isinstance(target_obj, Treasure):
                if isinstance(current_obj, Character) or isinstance(current_obj, Monster):
                    print(f"Move success and touch the treasure, type is {target_obj.type.value}")
                    current_obj.change_state(target_obj.touch_action(current_obj))
                    self.grid[new_y][new_x] = None
            else:
                print("Move success but there is an obstacle")
                return True # 有障礙物不移動

        self.grid[obj.position.y][obj.position.x] = None
        obj.position.x = new_x
        obj.position.y = new_y
        self.grid[new_y][new_x] = obj
        return True

    def get_character(self) -> Character:
        for row in self.grid:
            for cell in row:
                if isinstance(cell, Character):
                    return cell
        return None
    
    def get_monsters(self) -> List[Monster]:
        return [
            cell for row in self.grid for cell in row 
            if isinstance(cell, Monster)
        ]

    def get_objects_in_range(self, position: Position, attack_range: int, directions: List[Direction]) -> List[MapObject]:
        x, y = position.x, position.y
        objects_in_range = []

        for direction in directions:
            for i in range(1, attack_range + 1):
                if direction == Direction.UP:
                    new_x, new_y = x, y - i
                elif direction == Direction.DOWN:
                    new_x, new_y = x, y + i
                elif direction == Direction.LEFT:
                    new_x, new_y = x - i, y
                elif direction == Direction.RIGHT:
                    new_x, new_y = x + i, y

                if self.is_within_bounds(new_x, new_y):
                    obj = self.grid[new_y][new_x]
                    if obj is not None:
                        if isinstance(obj, Obstacle):
                            break
                        objects_in_range.append(obj)
                else:
                    break

        return objects_in_range
    
    def get_empty_positions(self) -> List[Position]:
        return [
            Position(x, y) for y, row in enumerate(self.grid) for x, cell in enumerate(row) if cell is None
        ]