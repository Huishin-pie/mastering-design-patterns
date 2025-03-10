from typing import List, Union
from enum import Enum

from player.player import Player
from deck.deck import Deck
from card.card import Card, Suit, Rank
from validate.validate_handler import ValidateHandler
from card_pattern.card_pattern import CardPattern


class MessageType(Enum):
    WINNER = "winner"
    NEW_ROUND = "new_round"
    CURRENT_PLAYER  = "player"
    HAND_CARDS = "hand_cards"
    ILLEGAL = "illegal"
    PASS = "pass"
    CANNOT_PASS = "cannot_pass"
    PLAYED_CARD_PATTERN = "card_pattern"
    DECK_CARDS = "deck_cards"


class Big2():
    PLAYERS_QTY = 4

    def __init__(self, players: List[Player], validate_handler: ValidateHandler):
        self.players = sorted(players, key=lambda player: (player.order))
        self.validate_handler = validate_handler
        self.deck: Deck = self._create_deck()
        self.top_player :Player = None
        self.current_player :Player = None
        self.top_play :CardPattern = None
        self.round = 1
    
    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        if len(value) != self.PLAYERS_QTY:
            raise ValueError(f"Players must be {self.PLAYERS_QTY}.")
        self._players = value
        
    def _create_deck(self):
        while True:
            input_value = input("請輸入牌堆的牌: ")
            
            try:
                card_list = input_value.split()
                
                if not card_list:
                    print("輸入不能為空，請重新輸入")
                    continue
                
                cards = []
                for card in card_list:
                    rank_str  = card.split("[")[1].split("]")[0]
                    rank = Rank.from_display(rank_str)
                    suit_str =  card[0]
                    suit = Suit.from_display(suit_str)
                    
                    if rank and suit:
                        cards.append(Card(rank, suit))
                
                return Deck(cards)
                
            except ValueError:
                print("無效的輸入，請確保輸入的是有效的牌")

    def start(self):
        for player in self.players:
            player.name_self()
        
        while self.deck.cards:
            for player in self.players:
                if not self.deck.cards:
                    return
                player.hand_cards.append(self.deck.deal())
        
        for player in self.players:
            player.hand_cards.sort(key=lambda card: (card.rank.value, card.suit.value))
        
        self.take_turn()
        
        self.out_put_message(MessageType.WINNER)

    def take_turn(self):
        while not self.game_end():
            self.out_put_message(MessageType.NEW_ROUND)
            
            self.get_current_player()
            self.clear_top_play()
            
            pass_count = 0
            
            while pass_count < 3:
                self.out_put_message(MessageType.CURRENT_PLAYER)
                
                is_pass = self.play_turn()

                if self.game_end():
                    return

                if is_pass:
                    pass_count += 1
                else:
                    pass_count = 0

                self.get_next_player()
            
            self.round += 1

    def play_turn(self) -> bool:
        self.out_put_message(MessageType.HAND_CARDS)
        
        while True:
            played_card = self.current_player.play_or_pass()
        
            if played_card is None:
                if self.top_play is not None:
                    self.out_put_message(MessageType.PASS)
                    return True
                else:
                    self.out_put_message(MessageType.CANNOT_PASS)
                    continue
                
            card_pattern = self.validate_play(played_card)

            if not card_pattern or (self.top_play is None and self.round == 1 and not self.has_club3(played_card)):
                self.out_put_message(MessageType.ILLEGAL)
                continue
            
            self.top_play = card_pattern
            self.top_player = self.current_player 
            
            for card in played_card:
                if card in self.current_player.hand_cards:
                    self.current_player.hand_cards.remove(card)
        
            self.out_put_message(MessageType.PLAYED_CARD_PATTERN)   
            return False
        
    def out_put_message(self, type: str):
        if type == MessageType.NEW_ROUND:
            print("新的回合開始了。")
            
        elif type == MessageType.WINNER:
            print(f"遊戲結束，遊戲的勝利者為 {self.top_player}")
            
        elif type == MessageType.CURRENT_PLAYER:
            print(f"輪到{self.current_player}了")
            
        elif type == MessageType.HAND_CARDS:
            print(self.format_cards(self.current_player.hand_cards))
            
        elif type == MessageType.ILLEGAL:
            print("此牌型不合法，請再嘗試一次。")
            
        elif type == MessageType.PASS:
            print(f"玩家 {self.current_player} PASS")
            
        elif type == MessageType.CANNOT_PASS:
            print("你不能在新的回合中喊 PASS")
            
        elif type == MessageType.PLAYED_CARD_PATTERN:
            print(f"玩家 {self.current_player} 打出了 {str(self.top_play)}")

    def clear_top_play(self):
        self.top_play = None

    def game_end(self) -> bool:
        return any(len(player.hand_cards) == 0 for player in self.players)
            
    def validate_play(self, cards: List[Card]) -> Union[CardPattern, bool]:
        new_card_pattern = self.validate_handler.validate(cards, self.top_play)
        if new_card_pattern is not None:
            return new_card_pattern
        else:
            return False
        
    def get_current_player(self):
        if self.round == 1:
            for player in self.players:
                if self.has_club3(player.hand_cards):
                    self.current_player = player
                    break
        else:
            self.current_player = self.top_player
    
    def get_next_player(self):
        self.current_player = self.players[(self.current_player.order + 1) % len(self.players)]
        
    def format_cards(self, cards: List[Card]):
        formatted_cards = [str(card) for card in cards]
        indices = " ".join(f"{i:<{len(formatted_cards[i])}}" for i in range(len(cards)))
        formatted_cards = " ".join(str(card) for card in cards)
        return f"{indices}\n{formatted_cards}"
        
    def has_club3(self, cards: List[Card]) -> bool:
        return any(card.suit == Suit.CLUB and card.rank == Rank.THREE for card in cards)
        
            
                
            
            
            
        
        
        
        
        
        
        
        
        
        