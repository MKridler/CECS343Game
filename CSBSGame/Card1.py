from Deck import Deck
from Player import Player


class Card1(Deck, Player):
    def play(self, player):
        # print(player.getLocation())
        if player.location != 'ECS 302' and player.location != 'ECS 308':
            player.setQP(-2)
        else:
            player.setLearning(1)

        # print(player.getLearning())
