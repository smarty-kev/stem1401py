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
frameUpper.pack(fill=BOTH, expand=True)

frameLower = Frame(root, bg="white")
frameLower.pack(fill=BOTH, expand=True)

root.mainloop()

