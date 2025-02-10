from abc import ABC, abstractmethod
from typing import List

from .player_template import PlayerTemplate
from .deck_template import DeckTemplate


class GameTemplate(ABC):

    def __init__(self, players: List[PlayerTemplate], deck: DeckTemplate):
        self.players = sorted(players, key=lambda player: (player.order))
        self.deck = deck
        self.winner: PlayerTemplate = None


    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        if len(value) < 2 or len(value) > 4:
            raise ValueError("Players must be between 2 and 4.")
        self._players = value

    @abstractmethod
    def draw_end(self) -> bool:
        pass

    @abstractmethod
    def before_player_turn(self):
        pass

    @abstractmethod
    def game_end(self) -> bool:
        pass

    @abstractmethod
    def execute_turn(self):
        pass

    @abstractmethod
    def get_winner(self) -> PlayerTemplate:
        pass

    @abstractmethod
    def show_winner(self):
        pass

    def start(self):
        print("☆☆☆☆☆ Game start ☆☆☆☆☆")

        for player in self.players:
            player.name_self()
            print(player)

        self.deck.shuffle()

        while(not self.draw_end()):  # hook()
            for player in self.players:
                player.get_hand_card(self.deck)

        self.before_player_turn()  # hook()

        round = 1
        while(not self.game_end()):  # hook()
            print(
                f"Round {round} start----------------------------------------")

            for player in self.players:
                player.take_turn(self.deck)  # hook()
                if self.game_end():  # hook()
                    print("break_game")
                    break

            self.deck.execute_turn()  # hook()
            self.execute_turn()  # hook()
            round += 1

        self.winner = self.get_winner()  # hook()
        self.show_winner()  # hook()

    def check_all_players_cards(self, card_qty: int):
        return all(len(player.cards) == card_qty for player in self.players)
