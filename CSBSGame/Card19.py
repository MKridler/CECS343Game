from Deck import Deck
from Player import Player


class Card19(Deck, Player):

    def play(self, player):
        if player.location != 'CECS Conference Room':
            player.setQP(-2)
        if player.integrity >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)
