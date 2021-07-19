"""

"""

from tkinter import *

root = Tk()
# root.geometry("800x450+200+200")
root.configure(bg="#ddddff")

colors = ["red", "orange", "yellow", "green","cyan", "blue", "purple"]

row = 0

# labels
for c in colors:
    Label(root, text=c, relief=GROOVE, width=25, height=3).grid(column=0, row=row)
    Label(root, bg=c, width=25, height=3).grid(column=1, row=row)
    row += 1


root.mainloop()
