__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card24(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Computer Lab':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 4:
            player.setQP(3)
            player.setCraft(1)
            return False
        else:
            return True