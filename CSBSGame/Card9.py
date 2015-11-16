__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card9(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Elevators':
            player.setQP(-2)
        else:
            player.setIntegrity(1)