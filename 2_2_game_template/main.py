from core.showdown_game import ShowdownGame

from core.uno_game import UnoGame


def showdown_main():
    try:
        game = ShowdownGame()
        game.start()
    except Exception as e:
        print(e)


def uno_main():
    try:
        game = UnoGame()
        game.start()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # showdown_main()
    uno_main()
