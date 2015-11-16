from Deck import Deck
from Player import Player


class Card8(Deck, Player):
    def play(self, player):
        if player.location != 'Forbidden Parking':
            player.setQP(-2)
        else:
            player.setLearning(1)
