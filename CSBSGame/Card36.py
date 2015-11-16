__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card36(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Computer Lab':
            player.setQP(-2)
        if player.getCraft() >= 2 and player.getIntegrity() >= 3:
            player.setQP(3)
            player.setIntegrity(1)
        else:
            player.setQP(-1)