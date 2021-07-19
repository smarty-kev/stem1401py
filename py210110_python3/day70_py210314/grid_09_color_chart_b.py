"""

"""

from tkinter import *

root = Tk()
# root.geometry("800x450+200+200")
root.configure(bg="#ddddff")

colors = ["red", "orange", "yellow", "green","cyan", "blue", "purple"]


# labels
for c in colors:
    Label(root, text=c, relief=GROOVE, width=25, height=3).grid(column=0, row=colors.index(c))
    Label(root, bg=c, width=25, height=3).grid(column=1, row=colors.index(c))

root.mainloop()
