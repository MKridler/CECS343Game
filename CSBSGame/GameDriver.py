from GameBoard import *
from Player import *
from tkinter import *
import random
root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title('BSCS Challenge')

player1 = Player('Donny', 'ECS 308', 0)
player2 = Player('Izzy', 'ECS 308',0)
player3 = Player('Jax', 'ECS 308',0)
playerlist = ['player1', 'player2', 'player3']

randUser = random.choice(playerlist)
#print(randUser)
if randUser == 'player1':
     player1.setAI(1)
     player2.setAI(0)
     player3.setAI(0)
elif randUser == 'player2':
    player2.setAI(1)
    player1.setAI(0)
    player3.setAI(0)
else:
    player3.setAI(1)
    player1.setAI(0)
    player2.setAI(0)


game = GameBoard(root, player1, player2, player3)

root.mainloop()
