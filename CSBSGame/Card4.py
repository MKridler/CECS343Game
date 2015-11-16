__author__ = 'DarthMerl'

from Deck import *
from Player import *

class Card4(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'ECS 302':
            player.setQP(-2)
        else:
            player.setLearning(1)