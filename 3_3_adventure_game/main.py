import traceback

from game.game import Game

def main():
    try:
        game = Game(10, 10)
        game.start()

    except Exception as e: 
        traceback.print_exc()

if __name__ == "__main__":
    main()