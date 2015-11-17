from tkinter import *
import tkinter.scrolledtext as tkst
#from Player import *
#from Rooms import *
import random
from __init__ import *


class GameBoard(Frame):
    moveCounter = 0

    def __init__(self,root,player1,player2, player3):
        self.root = root
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.playerlist = ()

        adjheight = (1/3) * root.winfo_screenheight()+30

        if player1.getAI() == 1:
            self.player = player1
            #self.hand(self.player)
            self.hand = Deck()
            self.hand2 = self.hand.deal(5)
            #print(self.player.ai,self.player.name, 'player hand', self.hand2)
            self.playerlist = (self.player, self.player2, self.player3)
        elif player2.getAI() == 1:
            self.player = player2
            #self.hand(self.player)
            self.hand = Deck()
            self.hand2 = self.hand.deal(5)
            #print(self.player.ai,self.player.name, 'player hand', self.hand2)
            self.playerlist = (self.player, self.player1, self.player3)
        else:
            self.player = player3
            #self.hand(self.player)
            self.hand = Deck()
            self.hand2 = self.hand.deal(5)
            #print(self.player.ai,self.player.name, 'player hand', self.hand2)
            self.playerlist = (self.player, self.player1, self.player2)



        #print(self.playerlist[0].getName())
        #print(self.player.getName())
        #self.create_board(root, player1, player2, player3)
        #self.buildMap(root, player1, player2, player3)
        self.frame = Frame(root, height = adjheight, width = 100)
        self.frame.pack(fill = BOTH, side = BOTTOM)
        self.frame.propagate(False)
        self.frame2 = Frame(self.frame,width = 100 )
        self.frame2.pack(side = RIGHT, anchor = NE)


        self.pane = PanedWindow(self.frame)
        self.pane.pack(anchor =NW)


        self.b = Button(self.pane, width = 10, text = 'Draw Card',command = lambda : self.drawCard())
        self.b.pack( pady = 5, anchor = W)

        self.card = Canvas(self.pane)
        element = self.hand2[0]
        img = element[2]

        self.photo = PhotoImage(file = img)
        #self.card.background = PhotoImage(file= 'card1.gif')
        self.card.create_image(50,0, anchor = NW, image = self.photo)
        self.card.bind("<Button-1>", self.changeCard)
        self.card.pack(side = RIGHT)



        #self.scrollbarTB = Scrollbar(self.frame2)
        #self.scrollbarTB.pack(side = RIGHT)
        self.text = Text(self.frame2,height = 8, width = 100)
        self.text.pack(padx = 50, pady = 10,anchor =E,  )


        self.stats(self.player1, self.player2, self.player3)

        self.text2 = tkst.ScrolledText(self.frame2,height = 3, width = 98)

        self.text2.pack(padx = 50, pady = 10, side = BOTTOM, anchor =SE)
        #self.scrollbarTB.config(command = self.text2.yview)
        self.scrollbarLB = Scrollbar(self.pane)
        self.scrollbarLB.pack(side = RIGHT)
        self.lb1 = Listbox(self.pane, selectmode = EXTENDED, yscrollcommand = self.scrollbarLB.set)
        self.text2.insert(END, '\n'+self.player.getName()+' is the user controlled player')

        self.scrollbarLB.config(command = self.lb1.yview)

        self.b1 = Button(self.pane, width = 10,state = DISABLED, text = 'Move', command = lambda : self.runClick(self.player))
        self.b1.pack(pady = 5, anchor = W)

        self.cardindex = element[1]
        #print('Main index',self.cardindex)
        self.b2 = Button(self.pane, width = 10,state = DISABLED,text = 'Play Card',command = lambda : self.playCard(self.cardindex))
        self.b2.pack(pady=5, anchor = W)

        self.vscrollbar = Scrollbar(root)
        self.vscrollbar.pack(side = RIGHT, fill = Y)
        self.hscrollbar= Scrollbar(root, orient = HORIZONTAL)
        self.hscrollbar.pack(side = BOTTOM, fill = X)

        self.w = Canvas(root, width = 1670, height = 2000,yscrollcommand = self.vscrollbar.set, xscrollcommand = self.hscrollbar.set)
        self.w.config(scrollregion=(0,0,1670, 2000))
        self.w.background = PhotoImage(file = 'CSULBMap3.gif')
        self.w.create_image(0,0, anchor = NW, image=self.w.background)

        self.token1 = self.w.create_text(850, 1350, fill = 'red', font =('Helvetica', 20), text = self.playerlist[0].getName())
        self.token2 = self.w.create_text(850, 1390, fill = 'red', font =('Helvetica', 20), text = self.playerlist[1].getName())
        self.token3 = self.w.create_text(850, 1430, fill = 'red', font =('Helvetica', 20), text = self.playerlist[2].getName())


        self.vscrollbar.config(command = self.w.yview)
        self.hscrollbar.config(command = self.w.xview)
        self.vscrollbar.pack()
        self.w.pack(expand = YES, side = LEFT, fill = BOTH)
        self.myRooms = Rooms()

        list1 = self.myRooms.roomConnections(player1.getLocation())

        for i in list1:
            self.lb1.insert(END, i)

        self.lb1.pack(side = LEFT, anchor = SW)

    def moves(self,player):

        self.myRooms = Rooms()
        list1 = self.myRooms.roomConnections(player.getLocation())

        for i in list1:
            self.lb1.insert(END, i)

    #def hand(self,player):

        #self.hand = Deck()
        #hand2 = self.hand.deal(5)
        #print(player.ai,player.name, 'player hand', hand2)


    def aiMover(self, player):
        print('AI working')
        #deck1 = Deck()
        #aiCard = deck1.aiDraw(player.getLocation())
        self.myRooms = Rooms()
        #print(player.getLocation())
        list1 = self.myRooms.roomConnections(player.getLocation())
        randloc = random.choice(list1)
        player.setLocation(randloc)
        newloc = self.myRooms.roomCoords(randloc)
        x = newloc[0]
        y = newloc[1]

        if player.getName() == self.playerlist[1].getName():
            deck1 = Deck()
            aiCard = deck1.aiDraw(player.getLocation())
            self.cardindex = aiCard[1]
            self.w.delete(self.token2)
            self.token2 = self.w.create_text(x, y+30, fill = 'red',font =('Helvetica', 20),text =  self.playerlist[1].getName())
            self.text2.insert(END, '\n'+player.getName()+' has moved to '+ player.getLocation())
            self.playCard(self.cardindex)
            self.player = self.playerlist[2]
            self.stats(self.player1, self.player2, self.player3)
            deck1.discard(aiCard)
            self.aiMover(self.player)
        elif player.getName() == self.playerlist[2].getName():
            deck1 = Deck()
            aiCard = deck1.aiDraw(player.getLocation())
            self.cardindex = aiCard[1]
            self.w.delete(self.token3)
            self.token3 = self.w.create_text(x, y+60, fill = 'red', font =('Helvetica', 20), text = self.playerlist[2].getName())
            self.text2.insert(END, '\n'+player.getName()+' has moved to '+ player.getLocation())
            self.playCard(self.cardindex)
            deck1.discard(aiCard)
            self.player = self.playerlist[0]
            self.stats(self.player1, self.player2, self.player3)
            self.b['state'] = 'normal'

    def runClick(self,player):
      GameBoard.moveCounter
      print(GameBoard.moveCounter)
      if GameBoard.moveCounter <3:
        items =self.lb1.curselection()
        value= self.lb1.get(items[0])

        player.setLocation(value)
        newloc = self.myRooms.roomCoords(value)
        x = newloc[0]
        y = newloc[1]

        self.lb1.delete(0, END)

        self.w.delete(self.token1)
        self.token1 = self.w.create_text(x, y, fill = 'red', font =('Helvetica', 20), text = self.playerlist[0].getName())
        self.moves(self.player)
        self.stats(self.player1, self.player2, self.player3)
        GameBoard.moveCounter = GameBoard.moveCounter +1
      if GameBoard.moveCounter == 3:
        #self.player = self.playerlist[1]
        self.b1['state'] = 'disabled'
        #self.aiMover(self.player)
        self.stats(self.player1, self.player2, self.player3)

    def teleport(self):
        self.lb1.delete(0, END)
        newloc = self.myRooms.roomCoords(self.player.getLocation())
        x = newloc[0]
        y = newloc[1]
        self.w.delete(self.token1)
        self.token1 = self.w.create_text(x, y, fill = 'red', font =('Helvetica', 20), text = self.playerlist[0].getName())
        self.moves(self.player)
        self.stats(self.player1, self.player2, self.player3)


    def changeCard(self,arg):
        lstlen = len(self.hand2)
        print('hand size: ',lstlen)
        element = self.hand2[0]
        print(element[2])
        img = element[2]
        self.cardindex = element[1]
        print(self.cardindex)
        self.hand2.append(element)
        self.hand2.remove(self.hand2[0])
        self.card.background = PhotoImage(file= img)
        self.card.create_image(50,0, anchor = NW, image = self.card.background)
        self.card.pack(side = RIGHT, fill = BOTH)
        self.stats(self.player1, self.player2, self.player3)

    def drawCard(self):
        self.b['state'] = 'disabled'
        self.b2['state'] = 'normal'
        self.b1['state'] = 'normal'
        decks = Deck()
        single = decks.draw()
        img = single[2]
        self.hand2.append(single)
        self.card.background = PhotoImage(file= img)
        self.card.create_image(50,0, anchor = NW, image = self.card.background)
        self.card.pack(side = RIGHT, fill = BOTH)
        self.stats(self.player1, self.player2, self.player3)

    def removeCard(self):
        decks = Deck()
        print(self.hand2[len(self.hand2)-1])
        decks.discard(self.hand2[len(self.hand2)-1])
        print('Removing')
        if len(self.hand2) > 1:
            element = self.hand2[1]
        else:
            element = self.hand2[0]
        img = element[2]
        self.hand2.remove(self.hand2[len(self.hand2)-1])
        #print(self.hand2)
        self.card.background = PhotoImage(file= img)
        self.card.create_image(50,0, anchor = NW, image = self.card.background)
        self.card.pack(side = RIGHT, fill = BOTH)
        #self.stats(self.player1, self.player2, self.player3)
        if self.player.getAI() == 1:
            self.player = self.playerlist[1]
            self.aiMover(self.player)

    def playCard(self, index):
        print('player AI: ',self.player.getAI())
        self.b1['state'] = 'disabled'
        self.b2['state'] = 'disabled'
        if index == 1:
            card1 = Card1()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)


        if index == 2:
            card1 = Card2()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 3:
            card1 = Card3()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 4:
            card1 = Card4()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 5:
            card1 = Card5()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 6:
            card1 = Card6()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 7:
            card1 = Card7()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 8:
            card1 = Card8()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
                print('removal complete')
                self.removeCard()
                print('removal complete')
            self.player.setLearning(1)
            self.stats(self.player1, self.player2, self.player3)

        if index == 9:
            card1 = Card9()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 10:
            card1 = Card10()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            print(result)
            if result == False:
                self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 11:
            card1 = Card11()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 12:
            card1 = Card12()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 13:
            card1 = Card13()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 14:
            card1 = Card14()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 15:
            card1 = Card15()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 16:
            card1 = Card16()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 17:
            card1 = Card17()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 18:
            card1 = Card18()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)


        if index == 19:
            card1 = Card19()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 20:
            card1 = Card20()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 21:
            card1 = Card21()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 22:
            card1 = Card22()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 23:
            card1 = Card23()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 24:
            card1 = Card24()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 25:
            card1 = Card25()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == 2:
                self.drawCard()
            if result == 3:
                if self.player.getAI() == 1:
                    self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 26:
            card1 = Card26()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 27:
            card1 = Card27()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                if self.player.getAI() == 1:
                    self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 28:
            card1 = Card28()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                if self.player.getAI() == 1:
                    self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 29:
            card1 = Card29()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 30:
            card1 = Card30()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == 2:
                if self.player.getAI() == 1:
                    self.drawCard()
            if result == 3:
                self.teleport()

                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 31:
            card1 = Card31()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                if self.player.getAI() == 1:
                    self.drawCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 32:
            card1 = Card32()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                if self.player.getAI() == 1:
                    self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 33:
            card1 = Card33()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == 2:
                if self.player.getAI() == 1:
                    self.drawCard()
                    self.drawCard()
            if result == 3:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 34:
            card1 = Card34()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 35:
            card1 = Card35()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 36:
            card1 = Card36()
            card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            self.stats(self.player1, self.player2, self.player3)

        if index == 37:
            card1 = Card37()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                if self.player.getAI() == 1:
                    self.removeCard()
            self.stats(self.player1, self.player2, self.player3)

        if index == 38:
            card1 = Card38()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

        if index == 39:
            card1 = Card39()
            result = card1.play(self.player)
            if self.player.getAI() == 1:
                self.removeCard()
            print('removal complete')
            if result == True:
                self.teleport()
                print('Teleporting')
            self.stats(self.player1, self.player2, self.player3)

    def stats(self, player1, player2, player3):
        self.text.delete(1.0, END)
        decks = Deck()
        size = decks.getDeckSize()
        discard = decks.getDiscardSize()
        #print(player1.getName())
        self.text.insert(INSERT, "          Learning    Crafts  Integrity   Quality Points")
        self.text.insert(INSERT, " \n" + player1.getName() + "        "+str(player1.getLearning()) + "          " + str(player1.getCraft()) + "          " + str(player1.getIntegrity()) + "             "+ str(player1.getQP()))
        self.text.insert(INSERT, " \n" + player2.getName() + "        "+str(player2.getLearning()) + "          " + str(player2.getCraft()) + "          " + str(player2.getIntegrity()) + "             "+ str(player2.getQP()))
        self.text.insert(INSERT, " \n" + player3.getName() + "        "+str(player3.getLearning()) + "          " + str(player3.getCraft()) + "          " + str(player3.getIntegrity()) + "             "+ str(player3.getQP()))
        self.text.insert(INSERT, " \n \nCards in Deck " + str(size)+ "       Cards in Discard Deck: "+ str(discard))
        self.text.insert(INSERT, " \nCurrent Player: "+ self.player.getName() +" located at "+ self.player.getLocation())