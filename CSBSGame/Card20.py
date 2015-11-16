__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card20(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
        if player.getCraft() >= 5:
            player.setQP(5)
        else:
            player.setQP(-3)