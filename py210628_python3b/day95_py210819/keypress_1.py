"""
Keypress
a-z, 1-9, other printable characters

event.x
event.y
event.char
"""

from tkinter import *


def press(event):
    print(f"You have pressed the key : {event.char}, keycode : {event.keycode}")


root = Tk()
root.title("Event Handling")
root.geometry("640x480+300+300")
root.config()

# root
root.bind("<Key>", press)

root.mainloop()
