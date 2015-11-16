__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card2(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Library':
            player.setQP(-2)
        else:
            player.setLearning(1)
