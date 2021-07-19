"""
place_04.py
layout manager
place
relwidth, relheight
range: 0 - 1
"""
from tkinter import *
root = Tk()
root.title('Python GUI - place')
root.geometry('640x480+300+300')
root.config(bg='#ddddff')
p1 = Label(root, text = 'Labele 1')
p2 = Label(root, text ='Labele 2')
p1.place(x=10, y=50)
# p2 does not show
p2.place(x=50, y=100, relx=0.2, rely=0.2,
         relwidth=0.2, relheight=0.2,
         anchor=CENTER)
root.mainloop()