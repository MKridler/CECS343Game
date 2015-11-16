from Deck import Deck
from Player import Player


class Card17(Deck, Player):

    def play(self, player):
        if player.location != 'ECS 308' and player.location != 'ECS 302':
            player.setQP(-2)
            return False
        if player.learning >= 5:
            player.setQP(5)
            return False
        else:
            player.setQP(-3)
            return True
