from typing import List
import random

from .deck_template import DeckTemplate
from models.uno_card import UnoCard


class UnoDeck(DeckTemplate):
    CARDS_QTY = 40

    def __init__(self, cards: List[UnoCard]):
        super().__init__(cards)


    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value):
        if len(value) == 0 or len(value) > self.CARDS_QTY:
            raise ValueError(
                f"The quantity of cards must equal {self.CARDS_QTY}.")
        self._cards = value

    def accept_play(self, card: UnoCard):
        last_played_card = self.get_last_played_card()
        if last_played_card.color == card.color or last_played_card.num == card.num:
            self.played_cards.append(card)
            return True
        else:
            print("Card is not avaliable. Please play a card again.")
            return False

    def draw_card(self):
        if len(self.cards) == 0:
            if len(self.played_cards) > 0:
                last_played_card = self.played_cards.pop(-1)
            else:
                raise ValueError(
                    "No cards available in played_cards to reshuffle.")

            self.cards.extend(self.played_cards)
            self.played_cards.clear()
            self.played_cards.append(last_played_card)

            self.shuffle()

        num = random.randint(0, len(self.cards)-1)
        return self.cards.pop(num)

    def execute_turn(self):
        self.show_last_played_card()

    def get_last_played_card(self) -> UnoCard:
        if not self.played_cards:
            raise ValueError(
                "Cannot show last played card: played_cards is empty.")
        return self.played_cards[-1]

    def show_last_played_card(self):
        print(f"Last played card: {self.get_last_played_card()}")

    def init_first_played_card(self):
        if not self.cards:
            raise ValueError(
                "Cannot initialize first played card: cards is empty.")
        self.played_cards.append(self.cards.pop())
