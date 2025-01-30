from models.individual import Individual, Gender
from .matchmaking_strategy import MatchmakingStrategy


class MatchmakingSystem:

    def __init__(self, target: Individual, strategy: MatchmakingStrategy):
        self.target = target
        self.strategy = strategy
        self.individuals = [
            Individual(1, Gender.MALE, 20, '', 'a,b,c', '1,1'),
            Individual(2, Gender.MALE, 20, '', 'a', '2,2'),
            Individual(3, Gender.MALE, 20, '', 'c', '3,3'),
            Individual(4, Gender.MALE, 20, '', 'b,c', '4,4'),
        ]


    def match(self):
        result = self.strategy.match(self.target, self.individuals)
        return result[0]