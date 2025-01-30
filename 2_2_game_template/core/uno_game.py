from .game_template import GameTemplate
from .uno_player import UnoPlayer
from .uno_deck import UnoDeck
from models.uno_card import UnoCard, Color, Num
from core.uno_ai_player import UnoAIPlayer
from core.uno_human_player import UnoHumanPlayer


class UnoGame(GameTemplate):

    def __init__(self):
        card_list = []
        for color in Color:
            for num in Num:
                card_list.append(UnoCard(num, color))

        deck = UnoDeck(card_list)

        players = [
            UnoHumanPlayer(1),
            UnoAIPlayer(2),
            UnoAIPlayer(3),
            # UnoAIPlayer(4)
        ]
        super().__init__(players, deck)
        

    def draw_end(self):
        return self.check_all_players_cards(5)

    def before_player_turn(self):
        self.deck.init_first_played_card()
        self.deck.show_last_played_card()

    def game_end(self):
        return self.player_has_no_card()

    def show_winner(self):
        print(f"Winner is {self.winner.name}, order: {self.winner.order}.")

    def get_winner(self):
        return self.get_no_card_player()

    def player_has_no_card(self):
        return any(len(player.cards) == 0 for player in self.players)

    def get_no_card_player(self) -> UnoPlayer:
        for player in self.players:
            if len(player.cards) == 0:
                return player
        raise ValueError("Not found no card player.")

    def execute_turn(self):
        pass
