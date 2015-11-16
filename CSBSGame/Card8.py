__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card8(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Forbidden Parking':
            player.setQP(-2)
        else:
            player.setLearning(1)