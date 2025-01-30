from .game_template import GameTemplate
from .showdown_deck import ShowdownDeck
from models.showdown_card import ShowdownCard, Suit, Rank
from core.showdown_ai_player import ShowdownAIPlayer
from core.showdown_human_player import ShowdownHumanPlayer


class ShowdownGame(GameTemplate):

    def __init__(self):
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(ShowdownCard(rank, suit))

        deck = ShowdownDeck(cards)

        players = [
            ShowdownHumanPlayer(1),
            ShowdownAIPlayer(2),
            ShowdownAIPlayer(3),
            ShowdownAIPlayer(4)
        ]
        super().__init__(players, deck)
        

    def draw_end(self):
        return self.check_all_players_cards(13)

    def before_player_turn(self):
        pass

    def game_end(self):
        return self.check_all_players_cards(0)

    def show_winner(self):
        print(
            f"Winner is {self.winner.name}, order: {self.winner.order}, point: {self.winner.point}.")

    def get_winner(self):
        return sorted(self.players, key=lambda palyer: (-palyer.point))[0]

    def execute_turn(self):
        player_dict = {player.order: player for player in self.players}
        for order in self.deck.round_winner_order:
            if order in player_dict:
                player = player_dict[order]
                player.point += 1
                print(f"Round winner: {player}")
