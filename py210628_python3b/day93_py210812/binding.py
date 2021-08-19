"""
Event binding and handling
button
"""

from tkinter import *


def atk():
    print("This is attack action")


root = Tk()
root.title("Python | Attack Handling")
root.geometry("640x480+200+200")

btn1 = Button(text="My btn", command=atk)
btn1.pack()


root.mainloop()
