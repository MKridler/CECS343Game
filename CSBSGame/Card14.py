from Deck import Deck
from Player import Player


class Card14(Deck, Player):

    def play(self, player):
        if player.location != 'ECS 308':
            player.setQP(-2)
        if player.craft >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)
