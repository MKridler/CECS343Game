from Deck import Deck
from .Player import Player


class Card15(Deck, Player):

    def play(self, player):
        if player.location != 'Pyramid':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True
