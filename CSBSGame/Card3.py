__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card3(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Library':
            player.setQP(-2)
        else:
            player.setIntegrity(1)