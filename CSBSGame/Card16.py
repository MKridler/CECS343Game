from Deck import Deck
from .Player import Player


class Card16(Deck, Player):

    def play(self, player):
        if player.location != 'George Allen Field':
            player.setQP(-2)
            return False
        if player.integrity >= 4:
            player.setCraft(2)
            return False
        else:
            player.setLocation('Room of Retirement')
            return True
