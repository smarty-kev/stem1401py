"""
Layout manager:  pack()
side=LEFT
start from left side
from left to right
"""
from tkinter import *
root = Tk()
label1 = Label(root, text='Python')
label2 = Label(root, text='Java',bg='yellow', font=(40))
label3 = Label(root, text='Web')
label4 = Label(root, text='Database',bg='yellow', font=(40))
root.geometry('640x480+0+0')
root.config(bg='#ddddff')
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack(side=LEFT)
root.mainloop()