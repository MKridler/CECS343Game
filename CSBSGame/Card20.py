from Deck import Deck
from Player import Player


class Card20(Deck, Player):

    def play(self, player):
        if player.location != 'George Allen Field':
            player.setQP(-2)
        if player.craft >= 5:
            player.setQP(5)
        else:
            player.setQP(-3)
