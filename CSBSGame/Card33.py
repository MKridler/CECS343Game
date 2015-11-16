__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card33(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'ECS 302' and player.getLocation() != 'ECS 308' and \
                player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall' and player.getLocation() != 'EAT Club' and \
                player.getLocation() != 'Computer Lab' and \
                player.getLocation() != 'CECS Conference Room' and player.getLocation() != 'Room of Retirement' and \
                player.getLocation() != 'Elevators':
            player.setQP(-2)
            return 1
        if player.getLearning() >= 3:
            player.setQP(5)
            return 2
        else:
            player.setQP(-5)
            player.setLocation('Lactation Lounge')
            return 3