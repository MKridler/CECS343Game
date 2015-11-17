import random
from Cards import *

class Deck(object):
    decksize = 0
    discardDeck = []
    activeDeck = []

    def __init__(self):
        # self.discard()
        # self.deck()
        # self.deal(value)
        #self.data2 = []

        # self.setdeckSize(0)

        Card1 = ("CECS 105", 1, 'CECS105.gif')
        Card2 = ("Research Compilers", 2, 'ResearchCompilers.gif')
        Card3 = ("Math 122", 3, 'Math122.gif')
        Card4 = ("Professor Murgolo's CECS 174 Class", 4, 'ProfMurgolo.gif')
        Card5 = ("Lunch at Bratwurst Hall", 5, 'LunchBrat.gif')
        Card6 = ("CECS 100", 6, 'CECS100.gif')
        Card7 = ("Exercising Mind and Body", 7, 'ExMindBody.gif')
        Card8 = ("Parking Violation", 8, 'ParkViolate.gif')
        Card9 = ("Finding the Lab", 9, 'FindLab.gif')
        Card10 = ("Goodbye, Professor", 10, 'ByeProf.gif')
        Card11 = ("Enjoying the Peace", 11, 'EnjoyPeace.gif')
        Card12 = ("Buddy Up", 12, 'BuddyUp.gif')
        Card13 = ("Late for Class", 13, 'Late4Class.gif')
        Card14 = ("Physics 151", 14, 'Phys151.gif')
        Card15 = ("The Big Game", 15, 'BigGame.gif')
        Card16 = ("KIN 253", 16, 'Kin253.gif')
        Card17 = ("Math 123", 17, 'Math123.gif')
        Card18 = ("Learning Netbeans", 18, 'LearnNetbeans.gif')
        Card19 = ("Choosing a Major", 19, 'ChooseMajor.gif')
        Card20 = ("Pass Soccer Class", 20, 'PassSoccer.gif')
        Card21 = ("Score a Goal!", 21, 'ScoreGoal.gif')
        Card22 = ("Fall in the Pond", 22, 'FallPond.gif')
        Card23 = ("Make the Dean's List", 23, 'DeanList.gif')
        Card24 = ("A  Laptop", 24, 'Laptop.gif')
        Card25 = ("Meet the Dean", 25, 'MeetDean.gif')
        Card26 = ("Loud Buzzing", 26, 'LoudBuzz.gif')
        Card27 = ("Program Crashes", 27, 'ProgramCrash.gif')
        Card28 = ("Professor Englert", 28, 'ProfEnglert.gif')
        Card29 = ("Press the Right Floor", 29, 'PressFloor.gif')
        Card30 = ("Soccer Goalie", 30, 'SoccerGoalie.gif')
        Card31 = ("Elective Class", 31, 'Elective.gif')
        Card32 = ("Oral Communications", 32, 'OralComm.gif')
        Card33 = ("Professor Hoffman", 33, 'ProfHoff.gif')
        Card34 = ("CHEM 111", 34, 'Chem111.gif')
        Card35 = ("The Outpost", 35, 'Outpost.gif')
        Card36 = ("Learning Linux", 36, 'LearnLinux.gif')
        Card37 = ("Make a Friend", 37, 'MakeFriend.gif')
        Card38 = ("Enjoying Nature", 38, 'EnjoyNature.gif')
        Card39 = ("Student Parking", 39, 'StuPark.gif')
        self.data2 = [
            Card1,
            Card2,
            Card3,
            Card4,
            Card5,
            Card6,
            Card7,
            Card8,
            Card9,
            Card10,
            Card11,
            Card12,
            Card13,
            Card14,
            Card15,
            Card16,
            Card17,
            Card18,
            Card19,
            Card20,
            Card21,
            Card22,
            Card23,
            Card24,
            Card25,
            Card26,
            Card27,
            Card28,
            Card29,
            Card30,
            Card31,
            Card32,
            Card33,
            Card34,
            Card35,
            Card36,
            Card37,
            Card38,
            Card39]
        random.shuffle(self.data2)

    def setdeckSize(self, value):

        print('Value: ', value)

    def getDeckSize(self):
        #print('Getter: ',self.deckSize)
        Deck.activeDeck
        if Deck.activeDeck == 0:
            Deck.activeDeck = Deck.discardDeck
            random.shuffle(Deck.activeDeck)
        return len(Deck.activeDeck)

    def deal(self, value):
        # self.deck()
        random.shuffle(self.data2)
        #print ('herewersdf',self.data2)
        hand = []
        for i in range(value):
            hand.append(self.data2[i])
            self.data2.remove(self.data2[i])
            # print(self.data2)
        # print('here',hand)
        #print('Decksize: ',len(self.data2))

        Deck.activeDeck = self.data2
        Deck.decksize = (len(self.data2))

        Deck.discardDeck = []
        #print (decksize)
        return hand

    def draw(self):

        random.shuffle(Deck.activeDeck)
        single = Deck.activeDeck[0]
        Deck.activeDeck.remove(Deck.activeDeck[0])
        return single

    def aiDraw(self, location):
        for i in range(len(Deck.activeDeck)):
            element = Deck.activeDeck[i]
            if element[2] == location:
                Deck.activeDeck.remove(Deck.activeDeck[i])
                return element
            elif i == (len(Deck.activeDeck)-1):
                Deck.activeDeck.remove(Deck.activeDeck[i])
                return element

    def discard(self, card):
        #global discardDeck
        Deck.discardDeck.append(card)
        # return len(discardDeck)

    def getDiscardSize(self):
        #global discardDeck
        return len(Deck.discardDeck)

    def play(self):
        pass
