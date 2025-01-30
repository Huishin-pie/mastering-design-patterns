from abc import ABC, abstractmethod
from typing import List

from models.individual import Individual


class MatchmakingStrategy(ABC):

    @abstractmethod
    def match(self, target: Individual, individuals: List[Individual]) -> List[Individual]:
        pass