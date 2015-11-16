from Deck import Deck
from Player import Player


class Card5(Deck, Player):
    def play(self, player):
        if player.location != 'Bratwurst Hall':
            player.setQP(-2)
        else:
            player.setCraft(1)
