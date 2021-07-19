"""
create a window
then create two frames
each of them takes half of the area of the window
one bg = "color1"
other bg = "color2"

up and bottom
"""

from tkinter import *

root = Tk()
root.title("Python GUI - Frame")
root.geometry("240x150")
root.config(bg="#ddddff")

frameUpper = Frame(root, bg="black")
frameUpper.pack(fill=X)
# frameUpper.place(relheight=0.5)

Label(frameUpper, text="Label1", bg="white").pack()
Label(frameUpper, text="Label2", bg="white").pack(side=BOTTOM)

frameLower = Frame(root, bg="white")
frameLower.pack(fill=X)
# frameLower.place(relheight=0.5)

Label(frameLower, text="Label1", bg="white").pack(side=LEFT)
Label(frameLower, text="Label2", bg="white").pack(side=RIGHT)

root.mainloop()

