"""
label anchor

anchor
    n, e, s, w
    ne, nw, se, sw
    center

anchor
    tk.N,tk.S,W,E,NE,NW,SE,SW,CENTER
"""

# import tkinter as tk

from tkinter import *

root = Tk()
root.title("Python GUI - Label, Anchor")

winw = 640
winh = 480
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")
root.config(bg="#ddddff")


# create a label
label1 = Label(root, text="Text Label", width=50, height=3, anchor="n")

label1.pack()

label2 = Label(root, text="Second Text Label", width=30, height=5, anchor=NW)

label2.pack()

root.mainloop()