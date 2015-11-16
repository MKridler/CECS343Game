__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card25(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall':
            player.setQP(-2)
            return 1
        if player.getIntegrity() >= 3 and player.getCraft() >= 3 and player.getLearning() >= 3:
            player.setQP(5)
            return 2
        else:
            return 3