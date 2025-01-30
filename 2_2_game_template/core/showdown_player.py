from .player_template import PlayerTemplate
from .deck_template import DeckTemplate


class ShowdownPlayer(PlayerTemplate):

    def __init__(self, order: int):
        super().__init__(order)
        self.point = 0
        

    def name_self(self):
        pass

    def select_play_card(self, deck: DeckTemplate):
        pass

    def can_not_play_action(self, deck: DeckTemplate):
        pass
