__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card37(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 2:
            player.setIntegrity(1)
            player.setQP(3)
            return False
        else:
            return True