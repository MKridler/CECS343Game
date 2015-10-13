from tkinter import *
from Player import *
from Rooms import *
import random

class GameBoard(Frame):

    def __init__(self,root,player1,player2, player3):
        self.root = root
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3

        #self.create_board(root, player1, player2, player3)
        #self.buildMap(root, player1, player2, player3)
        self.frame = Frame(root, height = 350, width = 100)
        self.frame.pack(expand = YES,fill = BOTH, side = BOTTOM)
        self.frame.propagate(False)
        self.frame2 = Frame(self.frame,width = 100 )
        self.frame2.pack(side = RIGHT, anchor = NE)


        self.pane = PanedWindow(self.frame, height = 350)
        self.pane.pack(anchor =NW)


        self.b = Button(self.pane, width = 10, text = 'Draw Card')
        self.b.pack( pady = 5, anchor = W)
        self.card = Label(self.frame2)
        self.card.pack(side = LEFT)
        self.text = Text(self.frame2,height = 8, width = 100)
        self.text.pack(padx = 50, pady = 10,anchor =E,  )
        self.text2 = Text(self.frame2,height = 3, width = 100)
        self.text2.pack(padx = 50, pady = 10, side = BOTTOM, anchor =SE)
        self.lb1 = Listbox(self.pane, selectmode = EXTENDED)

        self.player = player1
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
        self.w.background = PhotoImage(file = 'img1.gif')
        self.w.create_image(0,0, anchor = NW, image=self.w.background)

        self.token1 = self.w.create_text(825, 1350, fill = 'red', font = 15, text = player1.getName())
        self.token2 = self.w.create_text(825, 1390, fill = 'red', font = 15, text = player2.getName())
        self.token3 = self.w.create_text(825, 1430, fill = 'red', font = 15, text = player3.getName())


        self.vscrollbar.config(command = self.w.yview)
        self.hscrollbar.config(command = self.w.xview)
        self.vscrollbar.pack()
        self.w.pack(expand = YES, side = LEFT, fill = BOTH)
        self.myRooms = Rooms()
        #print(player1.getLocation())
        list1 = self.myRooms.roomConnections(player1.getLocation())

        for i in list1:
            self.lb1.insert(END, i)
        #print (list1)




        self.lb1.pack(side = LEFT, anchor = SW)

    def moves(self,player):

        self.myRooms = Rooms()
        print(player.getLocation())
        list1 = self.myRooms.roomConnections(player.getLocation())

        for i in list1:
            self.lb1.insert(END, i)


    def aiMover(self, player):

        self.myRooms = Rooms()
        print(player.getLocation())
        list1 = self.myRooms.roomConnections(player.getLocation())
        randloc = random.choice(list1)
        player.setLocation(randloc)
        newloc = self.myRooms.roomCoords(randloc)
        x = newloc[0]
        y = newloc[1]

        if player.getName() == 'Izzy':
            self.w.delete(self.token2)
            self.token2 = self.w.create_text(x, y+20, fill = 'red', font = 15, text = 'Izzy')
            self.text2.insert(END, '\nIzzy has moved to '+ player.getLocation())
            self.player = self.player3
            self.aiMover(self.player)
        elif player.getName() == 'Jax':
            self.w.delete(self.token3)
            self.token3 = self.w.create_text(x, y+40, fill = 'red', font = 15, text = 'Jax')
            self.text2.insert(END, '\nJax has moved to '+ player.getLocation())
            self.player = self.player1

    def runClick(self,player):

        items =self.lb1.curselection()
        value= self.lb1.get(items[0])
        print(player.getName())
        #print (items)
        player.setLocation(value)
        newloc = self.myRooms.roomCoords(value)
        x = newloc[0]
        y = newloc[1]



        #self.token1 = self.w.create_text(x, y, fill = 'red', font = 15, text = 'Donny')
        self.lb1.delete(0, END)

        if player.getName() == 'Donny':
            self.w.delete(self.token1)
            self.token1 = self.w.create_text(x, y, fill = 'red', font = 15, text = 'Donny')
            self.moves(self.player)
            self.player = self.player2
            self.aiMover(self.player)