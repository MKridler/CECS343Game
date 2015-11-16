__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card21(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
            return False
        if player.getCraft() >= 3:
            player.setQP(5)
            player.setIntegrity(1)
            return False
        else:
            player.setLocation('Student Parking')
            return True