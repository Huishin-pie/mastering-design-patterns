from .uno_player import UnoPlayer
from .uno_deck import UnoDeck


class UnoHumanPlayer(UnoPlayer):

    def __init__(self, order: int):
        super().__init__(order)
        

    def name_self(self):
        self.name = input("Please enter your name:").strip()

    def select_play_card(self, deck: UnoDeck):
        playable_cards = self.get_can_play_cards(deck)
        print("Your playable cards:")
        for index, card in playable_cards.items():
            print(f"{index}: {card}")

        while True:
            try:
                played_card_index = int(
                    input("Please select a card: "))
                if played_card_index in playable_cards:
                    return self.cards[played_card_index]
                else:
                    print("Invalid index. Please select a valid card index.")
            except ValueError:
                print("Invalid input. Please enter a number.")
