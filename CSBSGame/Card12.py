from Deck import Deck
from Player import Player


class Card12(Deck, Player):
    def play(self, player):
        if (player.location != 'EAT Club' and
            player.location != 'George Allen Field'):
            player.setQP(-2)
        else:
            player.setCraft(1)
