__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card26(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'EAT Club':
            player.setQP(-2)
        if player.getCraft() >= 3:
            player.setIntegrity(1)
        else:
            player.setQP(-2)