__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card29(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Elevators':
            player.setQP(-2)
        if player.getLearning() >= 4:
            player.setCraft(2)
        else:
            player.setQP(-2)