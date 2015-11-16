__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card14(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'ECS 308':
            player.setQP(-2)
        if player.getCraft() >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)