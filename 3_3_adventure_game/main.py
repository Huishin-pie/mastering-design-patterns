import traceback

from game.game import Game
from map.map import Map

def main():
    try:
        map = Map(10, 10)
        game = Game(map)
        game.start()

    except Exception as e: 
        traceback.print_exc()

if __name__ == "__main__":
    main()