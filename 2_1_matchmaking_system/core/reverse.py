from typing import List

from .matchmaking_strategy import MatchmakingStrategy
from models.individual import Individual


class Reverse(MatchmakingStrategy):
    
    def __init__(self, strategy: MatchmakingStrategy):
        self.strategy = strategy


    def match(self, target: Individual, individuals: List[Individual]) -> List[Individual]:
        return self.strategy.match(target, individuals)[::-1]
