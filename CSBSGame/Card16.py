__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card16(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 4:
            player.setCraft(2)
            return False
        else:
            player.setLocation('Room of Retirement')
            return True