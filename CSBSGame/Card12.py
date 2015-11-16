__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card12(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'EAT Club' and player.getLocation() != 'George Allen Field':
            player.setQP(-2)
        else:
            player.setCraft(1)