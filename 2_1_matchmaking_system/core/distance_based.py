from typing import List
import math

from models.individual import Individual
from .matchmaking_strategy import MatchmakingStrategy


class DistanceBased(MatchmakingStrategy):

    def calculate_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def match(self, target: Individual, individuals: List[Individual]) -> List[Individual]:
        target_x, target_y = target.coord.split(',')

        sorted_individuals = sorted(individuals, key=lambda individual: (
            self.calculate_distance(float(target_x), float(target_y), 
                float(individual.coord.split(',')[0]), 
                float(individual.coord.split(',')[1])),
                individual.id
        ))

        return sorted_individuals