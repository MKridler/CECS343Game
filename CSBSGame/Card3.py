from Deck import Deck
from Player import Player


class Card3(Deck, Player):
    def play(self, player):
        if player.location != 'Library':
            player.setQP(-2)
        else:
            player.setIntegrity(1)
