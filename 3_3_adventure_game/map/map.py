from typing import List
import random

from map_object.map_object import MapObject, Position, Direction
from map_object.role import State
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

        init_map: List[List[MapObject | None]]  = [[None for _ in range(width)] for _ in range(height)]

        object_probabilities = {
            TreasureType.SUPER_STAR: 10,
            TreasureType.POISON: 25,
            TreasureType.ACCELERATING_POTION: 20,
            TreasureType.HEALING_POTION: 15,
            TreasureType.DEVIL_FRUIT: 10,
            TreasureType.KINGS_ROCK: 10,
            TreasureType.DOKODEMO_DOOR: 10
        }

        num_treasures = random.randint(4, 6)
        num_monsters = random.randint(4, 6)
        num_obstacles = random.randint(3, 5)

        occupied_positions = set()

        # Treasure
        for _ in range(num_treasures):
            while True:
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                if (x, y) not in occupied_positions:
                    break
            occupied_positions.add((x, y))

            treasure_type = random.choices(list(object_probabilities.keys()), weights=object_probabilities.values(), k=1)[0]
            treasure = Treasure(treasure_type)
            treasure.position = Position(x, y)
            init_map[y][x] = treasure

        # Monster
        for _ in range(num_monsters):
            while True:
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                if (x, y) not in occupied_positions:
                    break
            occupied_positions.add((x, y))

            monster = Monster(_)
            monster.position = Position(x, y)
            init_map[y][x] = monster

        # Obstacle
        for _ in range(num_obstacles):
            while True:
                x, y = random.randint(0, width - 1), random.randint(0, height - 1)
                if (x, y) not in occupied_positions:
                    break
            occupied_positions.add((x, y))

            obstacle = Obstacle()
            obstacle.position = Position(x, y)
            init_map[y][x] = obstacle

        # Character
        while True:
            x, y = random.randint(0, width - 1), random.randint(0, height - 1)
            if (x, y) not in occupied_positions:
                break
        occupied_positions.add((x, y))

        character = Character(attack_range=max(width, height))
        character.position = Position(x, y)
        init_map[y][x] = character

        return init_map

    def is_within_bounds(self, x: int, y: int) -> bool:
        return 0 <= y < self.height and 0 <= x < self.width
    
    def add_object(self, x, y, obj):
        if self.is_within_bounds(x, y):
            self.grid[y][x] = obj
        else:
            raise ValueError("Coordinates out of bounds")

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
            # print("Invalid direction")
            return False

        dx, dy = direction_map[direction]
        new_x = obj.position.x + dx
        new_y = obj.position.y + dy
        current_obj = self.grid[obj.position.y][obj.position.x]
        print(new_x, new_y)

        if not self.is_within_bounds(new_x, new_y):
            # print("not is_within_bounds")
            return False
        
        target_obj = self.grid[new_y][new_x]
        current_obj = self.grid[obj.position.y][obj.position.x]

        if target_obj:
            if isinstance(target_obj, Treasure):
                treasure_map = {
                    TreasureType.SUPER_STAR: State.INVINCIBLE,
                    TreasureType.POISON: State.POISONED,
                    TreasureType.ACCELERATING_POTION: State.ACCELERATED,
                    TreasureType.HEALING_POTION: State.HEALING,
                    TreasureType.DEVIL_FRUIT: State.ORDERLESS,
                    TreasureType.KINGS_ROCK: State.STOCKPILE,
                    TreasureType.DOKODEMO_DOOR: State.TELEPORT
                }
                if isinstance(current_obj, Character) or isinstance(current_obj, Monster):
                    print(f"Move success and touch the treasure, type is {target_obj.type}")
                    current_obj.change_state(treasure_map[target_obj.type], 3)
                    self.grid[new_y][new_x] = None
            else:
                print("Move success but there is an obstacle")
                return True # 有障礙物不移動

        self.grid[obj.position.y][obj.position.x] = None
        obj.position.x = new_x
        obj.position.y = new_y
        self.grid[new_y][new_x] = obj
        # print("Move success")
        return True
    
    def monsters_alive(self) -> bool:
        return any(
            isinstance(cell, Monster) 
            for row in self.grid for cell in row 
            if cell is not None
        )

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
    