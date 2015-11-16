from Deck import Deck
from Player import Player


class Card13(Deck, Player):

    def play(self, player):
        if player.location == 'Forbidden Parking' or player.location == 'ECS 302' or player.location == 'ECS 308' or \
                player.location == 'North Hall' or player.location == 'South Hall' or player.location == 'EAT Club' or \
                player.location == 'Lactation Lounge' or player.location == 'Computer Lab' or \
                player.location == 'CECS Conference Room' or player.location == 'Room of Retirement' or \
                player.location == 'Elevators':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True
