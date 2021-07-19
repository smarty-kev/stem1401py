"""
Layout manager:  pack()
side
homework: list bitmap from left to right
"""
from tkinter import *
from tkinter.ttk import Separator
root = Tk()
root.geometry('640x480+0+0')
root.config(bg='#ddddff')
bitmaps = ["error", "hourglass", "info", "questhead", "question",
           "warning", "gray12", "gray25", "gray50", "gray75"]
for mybitmap in bitmaps:
    Label(root,bitmap=mybitmap,
          fg="blue").pack(side=LEFT, padx=5, ipadx=10)
# mylabel.config(padx=0)
root.mainloop()