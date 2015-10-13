from GameBoard import *
from Player import *
from tkinter import *

root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

player1 = Player('Donny', 'ECS 308')
player2 = Player('Izzy', 'ECS 308')
player3 = Player('Jax', 'ECS 308')
playerlist = [player1, player2, player3]
#print (len(playerlist))
game = GameBoard(root, player1, player2, player3)

root.mainloop()
