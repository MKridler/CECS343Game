__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card31(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Library':
            player.setQP(-2)
            return False
        if player.getLearning() >= 2:
            player.setLearning(1)
            return True
        else:
            player.setQP(-2)
            return False