from core.matchmaking_system import MatchmakingSystem 
from models.individual import Individual, Gender
from core.habit_based import HabitBased
from core.distance_based import DistanceBased
from core.reverse import Reverse

def main():
    try:
        target = Individual(6, Gender.FEMALE, 20, '', 'b,c', '0,0')
        distance_strategy = DistanceBased()
        habit_strategy = HabitBased()
        reverse_strategy = Reverse(habit_strategy)
        match_system = MatchmakingSystem(target, reverse_strategy)

        result = match_system.match()
        print(f"Matched result is - id:{result.id}, coord:{result.coord}, habit:{result.habit}")
    
    except ValueError as e:
        print(f"Value error: {e}")

if __name__ == "__main__":
    main()