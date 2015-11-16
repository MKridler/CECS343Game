__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card10(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Room of Retirement':
            player.setQP(-2)
            return True
        if player.getCraft() >= 6 and player.getIntegrity() >=6 and player.getLearning() >=6:
            player.setQP(10)
            return True

        else:
            return False