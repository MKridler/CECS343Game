from Deck import Deck
from Player import Player


class Card18(Deck, Player):

    def play(self, player):
        if player.location != 'Lactation Lounge':
            player.setQP(-2)
        if player.learning >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)
