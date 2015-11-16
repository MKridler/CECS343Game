from tkinter import *
import tkinter.scrolledtext as tkst
from Player import *
from Rooms import *
import random

class GameBoard(Frame):

    def __init__(self,root,player1,player2, player3):
        self.root = root
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.playerlist = ()
        adjheight = (1/3) * root.winfo_screenheight()

        if player1.getAI() == 1:
            self.player = player1
            self.playerlist = (self.player, self.player2, self.player3)
        elif player2.getAI() == 1:
            self.player = player2
            self.playerlist = (self.player, self.player1, self.player3)
        else:
            self.player = player3
            self.playerlist = (self.player, self.player1, self.player2)

        #print(self.playerlist[0].getName())
        #print(self.player.getName())
        #self.create_board(root, player1, player2, player3)
        #self.buildMap(root, player1, player2, player3)
        self.frame = Frame(root, height = adjheight, width = 100)
        self.frame.pack(expand = YES,fill = BOTH, side = BOTTOM)
        self.frame.propagate(False)
        self.frame2 = Frame(self.frame,width = 100 )
        self.frame2.pack(side = RIGHT, anchor = NE)


        self.pane = PanedWindow(self.frame, height = 350)
        self.pane.pack(anchor =NW)


        self.b = Button(self.pane, width = 10, text = 'Draw Card')
        self.b.pack( pady = 5, anchor = W)

        #self.card = Canvas(self.pane, width = 200, height =270)
        #self.scrollbarTB = Scrollbar(self.frame2)
        #self.scrollbarTB.pack(side = RIGHT)
        self.text = Text(self.frame2,height = 8, width = 100)
        self.text.pack(padx = 50, pady = 10,anchor =E,  )
        self.text2 = tkst.ScrolledText(self.frame2,height = 3, width = 98)

        self.text2.pack(padx = 50, pady = 10, side = BOTTOM, anchor =SE)
        #self.scrollbarTB.config(command = self.text2.yview)
        self.scrollbarLB = Scrollbar(self.pane)
        self.scrollbarLB.pack(side = RIGHT)
        self.lb1 = Listbox(self.pane, selectmode = EXTENDED, yscrollcommand = self.scrollbarLB.set)
        self.text2.insert(END, '\n'+self.player.getName()+' is the user controlled player')

        self.scrollbarLB.config(command = self.lb1.yview)

        self.b1 = Button(self.pane, width = 10,text = 'Move', command = lambda : self.runClick(self.player))
        self.b1.pack(pady = 5, anchor = W)

        self.b2 = Button(self.pane, width = 10,text = 'Play Card')
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


    def aiMover(self, player):

        self.myRooms = Rooms()
        #print(player.getLocation())
        list1 = self.myRooms.roomConnections(player.getLocation())
        randloc = random.choice(list1)
        player.setLocation(randloc)
        newloc = self.myRooms.roomCoords(randloc)
        x = newloc[0]
        y = newloc[1]

        if player.getName() == self.playerlist[1].getName():
            self.w.delete(self.token2)
            self.token2 = self.w.create_text(x, y+30, fill = 'red',font =('Helvetica', 20),text =  self.playerlist[1].getName())
            self.text2.insert(END, '\n'+player.getName()+' has moved to '+ player.getLocation())
            self.player = self.playerlist[2]
            self.aiMover(self.player)
        elif player.getName() == self.playerlist[2].getName():
            self.w.delete(self.token3)
            self.token3 = self.w.create_text(x, y+60, fill = 'red', font =('Helvetica', 20), text = self.playerlist[2].getName())
            self.text2.insert(END, '\n'+player.getName()+' has moved to '+ player.getLocation())
            self.player = self.playerlist[0]

    def runClick(self,player):

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
        self.player = self.playerlist[1]
        self.aiMover(self.player)