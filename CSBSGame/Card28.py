__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card28(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'CECS Conference Room':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 3:
            player.setCraft(1)
            return False
        else:
            return True