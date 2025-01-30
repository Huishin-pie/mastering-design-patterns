from .player_template import PlayerTemplate
from .uno_deck import UnoDeck


class UnoPlayer(PlayerTemplate):

    def __init__(self, order: int):
        super().__init__(order)
        

    def name_self(self):
        pass

    def select_play_card(self, deck: UnoDeck):
        pass

    def can_not_play_action(self, deck: UnoDeck):
        print(
            f"[{self}] - No card to play. Player draw a card.")
        self.cards.append(deck.draw_card())

    def can_play(self, deck: UnoDeck) -> bool:
        last_played_card = deck.get_last_played_card()
        return any(card.color == last_played_card.color or card.num == last_played_card.num for card in self.cards)

    def get_can_play_cards(self, deck: UnoDeck) -> dict:
        result = {}
        last_card = deck.get_last_played_card()
        for index, card in enumerate(self.cards):
            if card.color == last_card.color or card.num == last_card.num:
                result[index] = card
        return result
