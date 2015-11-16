__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card7(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Rec Center':
            player.setQP(-2)
        else:
            player.setIntegrity(1)