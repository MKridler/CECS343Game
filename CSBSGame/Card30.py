__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card30(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
            return 1
        if player.getLearning() >= 3 and player.getCraft() >=3:
            player.setQP(5)
            return 2
        else:
            player.setLocation('Student Parking')
            return 3
