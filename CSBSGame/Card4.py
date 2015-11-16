from Deck import Deck
from Player import Player


class Card4(Deck, Player):
    def play(self, player):
        if player.location != 'ECS 302':
            player.setQP(-2)
        else:
            player.setLearning(1)
