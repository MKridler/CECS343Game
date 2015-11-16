from Deck import Deck
from Player import Player


class Card6(Deck, Player):
    def play(self, player):
        if player.location != 'ECS 308':
            player.setQP(-2)
        else:
            player.setCraft(1)
