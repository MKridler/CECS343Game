__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card15(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Pyramid':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True