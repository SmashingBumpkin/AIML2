import time
import random
import numpy as np


class Game:
    def __init__(self, number_of_players: int):
        self.players = [Player(i) for i in range(number_of_players)]
        print(self.players)

    def draw_card():
        return random.randint(2, 4)

    def play_round(self):
        somebody_drew = False
        for player in self.players:
            if player.next_move():
                somebody_drew = True
        return somebody_drew
    
    def play_game(self):
        game
        while 


class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []
        self.hand_value = 0

    def draw(self):
        card_value = Game.draw_card()
        self.hand.append(card_value)
        self.hand_value += card_value

    def next_move(self):
        if self.hand_value < 3:
            self.draw()
            return True
        return False


new_game = Game(3)
