__author__ = 'DarthMerl'
from Deck import *
from Player import *

class Card13(Deck, Player):
    def play(self, player):
        if player.getLocation() == 'Forbidden Parking' or player.getLocation() == 'ECS 302' or player.getLocation() == 'ECS 308' or \
                player.getLocation() == 'North Hall' or player.getLocation() == 'South Hall' or player.getLocation() == 'EAT Club' or \
                player.getLocation() == 'Lactation Lounge' or player.getLocation() == 'Computer Lab' or \
                player.getLocation() == 'CECS Conference Room' or player.getLocation() == 'Room of Retirement' or \
                player.getLocation() == 'Elevators':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True