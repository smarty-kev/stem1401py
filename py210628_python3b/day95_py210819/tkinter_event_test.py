"""
testing of different tkinter events and key names
"""

from tkinter import *


def leave(event):
    var.set(sad_face)
    root.title("Not UwU")


def enter(event):
    var.set(happy_face)
    root.title("UwU")


root = Tk()
root.title(":|")
root.geometry("140x140+300+300")
root.config()


happy_face = ":>"
neutral_face = ":|"
sad_face = ":<"
var = StringVar()
var.set(neutral_face)
emoji = Label(textvariable=var, font=(None, 150))
emoji.pack()

# root
root.bind("<Leave>", leave)

root.bind("<Enter>", enter)

root.mainloop()

