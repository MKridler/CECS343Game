from Deck import Deck
from Player import Player


class Card9(Deck, Player):
    def play(self, player):
        if player.location != 'Elevators':
            player.setQP(-2)
        else:
            player.setIntegrity(1)

