"""
Layout manager:  pack()
side=RIGHT
start from right side
from right to left
"""
from tkinter import *
root = Tk()
label1 = Label(root, text='Python')
label2 = Label(root, text='Java',bg='yellow', font=(40))
label3 = Label(root, text='Web')
label4 = Label(root, text='Database',bg='yellow', font=(40))
root.geometry('640x480+0+0')
root.config(bg='#ddddff')
label1.pack(side=RIGHT)
label2.pack(side=RIGHT)
label3.pack(side=RIGHT)
label4.pack(side=RIGHT)
root.mainloop()