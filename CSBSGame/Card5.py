__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card5(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Bratwurst Hall':
            player.setQP(-2)
        else:
            player.setCraft(1)