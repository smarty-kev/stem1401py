"""
Layout manager:  pack()
side=BOTTOM
start from bottom side
from bottom to top
"""
from tkinter import *
root = Tk()
label1 = Label(root, text='Python')
label2 = Label(root, text='Java',bg='yellow', font=(40))
label3 = Label(root, text='Web')
label4 = Label(root, text='Database',bg='yellow', font=(40))
root.geometry('640x480+0+0')
root.config(bg='#ddddff')
label1.pack(side=BOTTOM)
label2.pack(side=BOTTOM)
label3.pack(side=BOTTOM)
label4.pack(side=BOTTOM)
root.mainloop()