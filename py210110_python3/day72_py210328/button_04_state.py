"""
Button
state

normal
active
disabled
"""

from tkinter import *

def helloCallBack():
    pass


root = Tk()
root.geometry("800x450+200+200")
root.configure(bg="#ddddff")


# button
btn1 = Button(root, text="Normal", command=lambda : helloCallBack, state="normal")
btn1.pack()

btn2 = Button(root, text="Active", command=lambda : helloCallBack, state="active")
btn2.pack()

btn2 = Button(root, text="Disabled", command=lambda : helloCallBack, state="disabled")
btn2.pack()

root.mainloop()
