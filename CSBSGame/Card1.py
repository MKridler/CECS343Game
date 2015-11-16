__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card1(Deck,Player):
    def play(self, player):
        #print(player.getLocation())
        if player.getLocation() != 'ECS 302' and player.getLocation() != 'ECS 308':
            player.setQP(-2)
        else:
            player.setLearning(1)

        #print(player.getLearning())

