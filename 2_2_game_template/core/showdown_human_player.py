from .showdown_player import ShowdownPlayer
from .showdown_deck import ShowdownDeck


class ShowdownHumanPlayer(ShowdownPlayer):

    def __init__(self, order: int):
        super().__init__(order)
        

    def name_self(self):
        self.name = input("Please enter your name:").strip()

    def select_play_card(self, deck: ShowdownDeck):
        print("Your cards:")
        for index, card in enumerate(self.cards):
            print(f"{index}: {card}")

        while True:
            try:
                played_card_index = int(
                    input("Please select a card: "))
                if 0 <= played_card_index < len(self.cards):
                    return self.cards[played_card_index]
                else:
                    print("Invalid index. Please select a valid card index.")
            except ValueError:
                print("Invalid input. Please enter a number.")
