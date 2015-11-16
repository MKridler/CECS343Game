from Deck import Deck
from Player import Player


class Card10(Deck, Player):
    def play(self, player):
        if player.getLocation() != 'Room of Retirement':
            player.setQP(-2)
            return True
        if player.craft >= 6 and player.getIntegrity() >=6 and player.getLearning() >=6:
            player.setQP(10)
            return True

        else:
            return False
