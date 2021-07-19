"""
place_01_xy.py
layout manager
place
x, y
"""

from tkinter import *
root = Tk()

root.title('Python GUI - place')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')

p1 = Label(root, text = 'Labele 1')
p2 = Label(root, text ='Labele 2')

p1.place(x=100, y=100)
p2.place(x=200, y=20)


root.mainloop()
