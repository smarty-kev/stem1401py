"""
Event binding and handling
button
"""

from tkinter import *


def atk(event):
    print("This is attack action")
    print(event.x, event.y)


root = Tk()
root.title("Python | Attack Handling")
root.geometry("640x480+200+200")

btn1 = Button(text="My btn")
btn1.bind("<Button-1>", atk)

btn1.focus()
btn1.pack()

root.mainloop()
