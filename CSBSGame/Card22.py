__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card22(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Japanese Garden':
            player.setQP(-2)
            return False
        if player.getLearning() >= 3:
            player.setIntegrity(1)
            player.setCraft(1)
            return False
        else:
            player.setLocation('Lactation Lounge')
            return True