from Deck import Deck
from Player import Player


class Card7(Deck, Player):
    def play(self, player):
        if player.location != 'Rec Center':
            player.setQP(-2)
        else:
            player.setIntegrity(1)
