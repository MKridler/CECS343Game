from Deck import Deck
from Player import Player


class Card11(Deck, Player):
    def play(self, player):
        if player.location != 'Japanese Garden':
            player.setQP(-2)
        else:
            player.setIntegrity(1)
