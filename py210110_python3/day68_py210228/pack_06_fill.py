"""
Layout manager:  pack()
option - fill
fill = X
fill = Y
fill = BOTH
fill = NONE
"""
from tkinter import *
root = Tk()
root.title('Python GUI - pack fill')
root.geometry('640x480+0+0')
root.config(bg='#ddddff')
label1 = Label(root, text='Java 1', font=('Arial', 20), fg='red',bg='yellow')
label2 = Label(root, text='Python 2',bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Web 3', font=('Arial', 20), fg='red')
# label1.pack(side = LEFT)
label1.pack(side = LEFT, fill = Y)
label2.pack()
label3.pack(fill = X)
root.mainloop()