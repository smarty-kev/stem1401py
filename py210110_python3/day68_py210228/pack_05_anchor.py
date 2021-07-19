"""
anchor = E, W, S, N
pack(anchor = direction_value)
"""

from tkinter import *

root = Tk()
root.geometry('640x480+0+0')
root.configure(bg="#ddddff")

label1 = Label(root, text='< Last', font=('Arial', 20), fg='red')
label2 = Label(root, text='Next >',bg='yellow', font=('Arial', 20))
label3 = Label(root, text='Min', font=('Arial', 20), fg='red')
label4 = Label(root, text='Max',bg='yellow', font=('Arial', 20))

label1.pack(side=LEFT, anchor=S)
label2.pack(side=LEFT, anchor=S, padx = 10)

label3.pack(side=RIGHT, anchor=N)
label4.pack(side=RIGHT, anchor=N, padx = 10)

root.mainloop()
