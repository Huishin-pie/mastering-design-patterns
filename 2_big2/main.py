from big2.big2 import Big2
from validate.single_validate import SingleValidate
from validate.pair_validate import PairValidate
from validate.straight_validate import StraightValidate
from validate.fullhouse_validate import FullhouseValidate
from player.human import HumanPlayer

def main():
    try:
        players = [
            HumanPlayer(0),
            HumanPlayer(1),
            HumanPlayer(2),
            HumanPlayer(3),
        ]
        game = Big2(players, SingleValidate(PairValidate(StraightValidate(FullhouseValidate(None)))))
        game.start()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()