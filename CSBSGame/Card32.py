__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card32(Deck, Player):
    def play(self, player):
        if player.getLocation() == 'ECS 302' or player.getLocation() == 'ECS 308' or \
                player.getLocation() == 'North Hall' or player.getLocation() == 'South Hall' or player.getLocation() == 'EAT Club' or \
                player.getLocation() == 'Lactation Lounge' or player.getLocation() == 'Computer Lab' or \
                player.getLocation() == 'CECS Conference Room' or player.getLocation() == 'Room of Retirement' or \
                player.getLocation() == 'Elevators':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 4:
            player.setQP(4)
            player.setCraft(1)
            return False
        else:
            return True