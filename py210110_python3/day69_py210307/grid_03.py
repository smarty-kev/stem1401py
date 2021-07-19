"""
Tkinter
using grid layout
grid()
column & row
"""

from tkinter import *

root = Tk()
root.geometry("800x450+200+200")
root.configure(bg="#ddddff")

# labels
label1 = Label(root, text="Label 1", bg="yellow")
label2 = Label(root, text="Label 2", bg="gray")
label3 = Label(root, text="Label 3", bg="gray")
label4 = Label(root, text="Label 4", bg="yellow")

# show on screen
# row always +1 from before
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)
label4.grid(row=1, column=1)

root.mainloop()
