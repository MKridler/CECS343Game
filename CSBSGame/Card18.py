__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card18(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Lactation Lounge':
            player.setQP(-2)
        if player.getLearning() >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)