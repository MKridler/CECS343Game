__author__ = 'kridl_000'
from tkinter import *

root = Tk()

frame = Frame(root, height = 150)
frame.pack(side = BOTTOM)
frame2 = Frame(root, height = 150)
frame2.pack(side = BOTTOM, anchor = SE)
#top = Toplevel(frame)
pane = PanedWindow(root, width = 5, height = 150)
pane.pack(side = BOTTOM, anchor = NW)
text = Text(frame2, height= 8, width = 100)
text.pack(side = BOTTOM, anchor =SE, padx = 20)
text2 = Text(frame2, height= 5, width = 100)
text2.pack(side = BOTTOM, anchor =SE, padx = 20)
vscrollbar = Scrollbar(root)
vscrollbar.pack(side = RIGHT, fill = Y)
hscrollbar= Scrollbar(root, orient = HORIZONTAL)
hscrollbar.pack(side = BOTTOM, fill = X)

w = Canvas(root, width = 1670, height = 2000,yscrollcommand = vscrollbar.set, xscrollcommand = hscrollbar.set)
w.config(scrollregion=(0,0,1670, 2000))


photo = PhotoImage(file = 'img1.gif')
image = w.create_image(0,0, anchor = NW, image=photo)
#used to create text placement
#w.create_text(100,100, text = 'HELLO WORLD!')
vscrollbar.config(command = w.yview)
hscrollbar.config(command = w.xview)
vscrollbar.pack()
w.pack(side = LEFT, fill = BOTH)
b = Button(pane, width = 10, text = 'Draw Card')
b.pack(padx =15, pady = 5)
b1 = Button(pane, width = 10,text = 'Move')
b1.pack(pady = 5)
b2 = Button(pane, width = 10,text = 'Play Card')
b2.pack(pady=5)
root.mainloop()