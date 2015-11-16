__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card19(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'CECS Conference Room':
            player.setQP(-2)
        if player.getIntegrity() >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)