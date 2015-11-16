__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card23(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall':
            player.setQP(-2)
            return False
        if player.getLearning() >= 6:
            player.setQP(5)
            return False
        else:
            player.setLocation('Student Parking')
            return True