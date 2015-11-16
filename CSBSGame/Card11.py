__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card11(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Japanese Garden':
            player.setQP(-2)
        else:
            player.setIntegrity(1)