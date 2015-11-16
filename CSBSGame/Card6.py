__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card6(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'ECS 308':
            player.setQP(-2)
        else:
            player.setCraft(1)