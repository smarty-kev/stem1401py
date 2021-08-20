"""
testing of different tkinter events and key names
"""

from tkinter import *


def handler(event):
    global score
    score += 1
    var.set(score)


root = Tk()
root.title("Scroll wheel Event")
root.geometry("640x480+300+300")
root.config()

score = 0
var = StringVar()
var.set(score)
emoji = Label(textvariable=var, font=(None, 150))
emoji.pack()

# root
root.bind("<MouseWheel>", handler)

root.mainloop()

