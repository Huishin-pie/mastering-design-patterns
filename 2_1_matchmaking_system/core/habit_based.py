from typing import List

from models.individual import Individual
from .matchmaking_strategy import MatchmakingStrategy


class HabitBased(MatchmakingStrategy):

    def get_intersection_count(self, list_1: List[str], list_2: List[str]):
        return len(set(list_1) & set(list_2))
    
    def match(self, target: Individual, individuals: List[Individual]) -> List[Individual]:
        habits = target.habit.split(',')

        sorted_individuals = sorted(individuals, key=lambda individual: (
          -self.get_intersection_count(habits, individual.habit.split(',')),
          individual.id
        ))
        
        return sorted_individuals