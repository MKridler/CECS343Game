from Deck import Deck
from Player import Player


class Card1(Deck, Player):

    def play(self, player):
        # print(player.getLocation())
        if player.getLocation() != 'ECS 302' and player.getLocation() != 'ECS 308':
            player.setQP(-2)
        else:
            player.setLearning(1)

        # print(player.getLearning())


class Card2(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Library':
            player.setQP(-2)
        else:
            player.setLearning(1)


class Card3(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Library':
            player.setQP(-2)
        else:
            player.setIntegrity(1)


class Card4(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'ECS 302':
            player.setQP(-2)
        else:
            player.setLearning(1)


class Card5(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Bratwurst Hall':
            player.setQP(-2)
        else:
            player.setCraft(1)


class Card6(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'ECS 308':
            player.setQP(-2)
        else:
            player.setCraft(1)


class Card7(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Rec Center':
            player.setQP(-2)
        else:
            player.setIntegrity(1)


class Card8(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Forbidden Parking':
            player.setQP(-2)
        else:
            player.setLearning(1)


class Card9(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Elevators':
            player.setQP(-2)
        else:
            player.setIntegrity(1)


class Card10(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Room of Retirement':
            player.setQP(-2)
            return True
        if player.getCraft() >= 6 and player.getIntegrity() >= 6 and player.getLearning() >= 6:
            player.setQP(10)
            return True

        else:
            return False


class Card11(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Japanese Garden':
            player.setQP(-2)
        else:
            player.setIntegrity(1)


class Card12(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'EAT Club' and player.getLocation() != 'George Allen Field':
            player.setQP(-2)
        else:
            player.setCraft(1)


class Card13(Deck, Player):

    def play(self, player):
        if player.getLocation() == 'Forbidden Parking' or player.getLocation() == 'ECS 302' or player.getLocation() == 'ECS 308' or \
                player.getLocation() == 'North Hall' or player.getLocation() == 'South Hall' or player.getLocation() == 'EAT Club' or \
                player.getLocation() == 'Lactation Lounge' or player.getLocation() == 'Computer Lab' or \
                player.getLocation() == 'CECS Conference Room' or player.getLocation() == 'Room of Retirement' or \
                player.getLocation() == 'Elevators':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True


class Card14(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'ECS 308':
            player.setQP(-2)
        if player.getCraft() >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)


class Card15(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Pyramid':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True


class Card16(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 4:
            player.setCraft(2)
            return False
        else:
            player.setLocation('Room of Retirement')
            return True


class Card17(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'ECS 308' and player.getLocation() != 'ECS 302':
            player.setQP(-2)
            return False
        if player.getLearning() >= 5:
            player.setQP(5)
            return False
        else:
            player.setQP(-3)
            return True


class Card18(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Lactation Lounge':
            player.setQP(-2)
        if player.getLearning() >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)


class Card19(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'CECS Conference Room':
            player.setQP(-2)
        if player.getIntegrity() >= 3:
            player.setQP(5)
        else:
            player.setQP(-3)


class Card20(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
        if player.getCraft() >= 5:
            player.setQP(5)
        else:
            player.setQP(-3)


class Card21(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
            return False
        if player.getCraft() >= 3:
            player.setQP(5)
            player.setIntegrity(1)
            return False
        else:
            player.setLocation('Student Parking')
            return True


class Card22(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Japanese Garden':
            player.setQP(-2)
            return False
        if player.getLearning() >= 3:
            player.setIntegrity(1)
            player.setCraft(1)
            return False
        else:
            player.setLocation('Lactation Lounge')
            return True


class Card23(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall':
            player.setQP(-2)
            return False
        if player.getLearning() >= 6:
            player.setQP(5)
            return False
        else:
            player.setLocation('Student Parking')
            return True


class Card24(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Computer Lab':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 4:
            player.setQP(3)
            player.setCraft(1)
            return False
        else:
            return True


class Card25(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall':
            player.setQP(-2)
            return 1
        if player.getIntegrity() >= 3 and player.getCraft() >= 3 and player.getLearning() >= 3:
            player.setQP(5)
            return 2
        else:
            return 3


class Card26(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'EAT Club':
            player.setQP(-2)
        if player.getCraft() >= 3:
            player.setIntegrity(1)
        else:
            player.setQP(-2)


class Card27(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Lactation Lounge':
            player.setQP(-2)
            return False
        if player.getLearning() >= 2:
            player.setQP(5)
            player.setIntegrity(1)
            return False
        else:
            return True


class Card28(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'CECS Conference Room':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 3:
            player.setCraft(1)
            return False
        else:
            return True


class Card29(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Elevators':
            player.setQP(-2)
        if player.getLearning() >= 4:
            player.setCraft(2)
        else:
            player.setQP(-2)


class Card30(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'George Allen Field':
            player.setQP(-2)
            return 1
        if player.getLearning() >= 3 and player.getCraft() >= 3:
            player.setQP(5)
            return 2
        else:
            player.setLocation('Student Parking')
            return 3


class Card31(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Library':
            player.setQP(-2)
            return False
        if player.getLearning() >= 2:
            player.setLearning(1)
            return True
        else:
            player.setQP(-2)
            return False


class Card32(Deck, Player):

    def play(self, player):
        if player.getLocation() == 'ECS 302' or player.getLocation() == 'ECS 308' or \
                player.getLocation() == 'North Hall' or player.getLocation() == 'South Hall' or player.getLocation() == 'EAT Club' or \
                player.getLocation() == 'Lactation Lounge' or player.getLocation() == 'Computer Lab' or \
                player.getLocation() == 'CECS Conference Room' or player.getLocation() == 'Room of Retirement' or \
                player.getLocation() == 'Elevators':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 4:
            player.setQP(4)
            player.setCraft(1)
            return False
        else:
            return True


class Card33(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'ECS 302' and player.getLocation() != 'ECS 308' and \
                player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall' and player.getLocation() != 'EAT Club' and \
                player.getLocation() != 'Computer Lab' and \
                player.getLocation() != 'CECS Conference Room' and player.getLocation() != 'Room of Retirement' and \
                player.getLocation() != 'Elevators':
            player.setQP(-2)
            return 1
        if player.getLearning() >= 3:
            player.setQP(5)
            return 2
        else:
            player.setQP(-5)
            player.setLocation('Lactation Lounge')
            return 3


class Card34(Deck, Player):

    def play(self, player):
        if player.getLocation() == 'ECS 302' or player.getLocation() == 'ECS 308' or \
                player.getLocation() == 'North Hall' or player.getLocation() == 'South Hall' or player.getLocation() == 'EAT Club' or \
                player.getLocation() == 'Lactation Lounge' or player.getLocation() == 'Computer Lab' or \
                player.getLocation() == 'CECS Conference Room' or player.getLocation() == 'Room of Retirement' or \
                player.getLocation() == 'Elevators':
            player.setQP(-2)
            return False
        if player.getCraft() >= 6:
            player.setQP(5)
            return False
        else:
            player.setLocation('Student Parking')
            return True


class Card35(Deck, Player):

    def play(self, player):
        if player.getLocation() == 'Forbidden Parking' or player.getLocation() == 'ECS 302' or player.getLocation() == 'ECS 308' or \
                player.getLocation() == 'North Hall' or player.getLocation() == 'South Hall' or player.getLocation() == 'EAT Club' or \
                player.getLocation() == 'Lactation Lounge' or player.getLocation() == 'Computer Lab' or \
                player.getLocation() == 'CECS Conference Room' or player.getLocation() == 'Room of Retirement' or \
                player.getLocation() == 'Elevators':
            player.setQP(-2)
        else:
            player.setIntegrity(1)


class Card36(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Computer Lab':
            player.setQP(-2)
        if player.getCraft() >= 2 and player.getIntegrity() >= 3:
            player.setQP(3)
            player.setIntegrity(1)
        else:
            player.setQP(-1)


class Card37(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'North Hall' and player.getLocation() != 'South Hall':
            player.setQP(-2)
            return False
        if player.getIntegrity() >= 2:
            player.setIntegrity(1)
            player.setQP(3)
            return False
        else:
            return True


class Card38(Deck, Player):

    def play(self, player):
        if player.getLocation() == 'ECS 302' or player.getLocation() == 'ECS 308' or \
                player.getLocation() == 'North Hall' or player.getLocation() == 'South Hall' or player.getLocation() == 'EAT Club' or \
                player.getLocation() == 'Lactation Lounge' or player.getLocation() == 'Computer Lab' or \
                player.getLocation() == 'CECS Conference Room' or player.getLocation() == 'Room of Retirement' or \
                player.getLocation() == 'Elevators':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True


class Card39(Deck, Player):

    def play(self, player):
        if player.getLocation() != 'Student Parking':
            player.setQP(-2)
            return False
        else:
            player.setCraft(1)
            player.setLocation('Lactation Lounge')
            return True
