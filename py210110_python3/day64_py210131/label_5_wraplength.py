"""
Tkinter
place a label widget
wraplength = n (px)
"""
from tkinter import *
root = Tk()
root.title('Python GUI - Label wraplength')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')
# create a label widget
label1 = Label(root, text='Tkinter Label 1',
               height=3, width=40,
               anchor='ne',
               wraplength=10)
# show on screen
label1.pack()
# create a label widget
label2 = Label(root, text='Tkinter Label 2',
               height=7, width=20,
               anchor='sw',
               wraplength=30)
# show on screen
label2.pack()
# create a label widget
label3 = Label(root, text='Tkinter Label 3',
               height=7, width=20,
               anchor=CENTER,
               wraplength=80)
# show on screen
label3.pack()
root.mainloop()