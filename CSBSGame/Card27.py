__author__ = 'DarthMerl'

from Deck import *
from Player import *

class Card27(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Lactation Lounge':
            player.setQP(-2)
            return False
        if player.getLearning() >= 2:
            player.setQP(5)
            player.setIntegrity(1)
            return False
        else:
            return True