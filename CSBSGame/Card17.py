__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card17(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'ECS 308' and player.getLocation() != 'ECS 302':
            player.setQP(-2)
            return False
        if player.getLearning() >= 5:
            player.setQP(5)
            return False
        else:
            player.setQP(-3)
            return True