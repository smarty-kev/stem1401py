"""
Tkinter
using grid layout
grid()
column
"""

from tkinter import *

root = Tk()
root.geometry("800x450+200+200")
root.configure(bg="#ddddff")

# labels
label1 = Label(root, text="Label 1")
label2 = Label(root, text="Label 2")
label3 = Label(root, text="Label 3")
label4 = Label(root, text="Label 4")
label5 = Label(root, text="Label 5")

# show on screen
# row always +1 from before
label1.grid()
label2.grid(column=1)
label3.grid(column=2)
label4.grid(column=3)
label5.grid(column=4)

root.mainloop()
