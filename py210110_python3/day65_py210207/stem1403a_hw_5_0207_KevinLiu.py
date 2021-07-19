"""
[Homework]
Date: 2021-02-07
1. Try out label widget
Description:
create a window based on previous homework
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create at least 2 text Labels
set dimension, font, fg, bg, font and any other options you know.
create at least 2 bitmap Labels
set dimension, fg, bg, font and any other options you know.
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Homework Kevin")


# window dimensions
winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


# window background color
root.configure(background="gray1")


# window -> topmost
root.wm_attributes("-topmost", True)


# window maxsize and minsize
root.maxsize(1920, 1080)
root.minsize()


# window -> resizable
root.resizable(1, 1)


# label
textlabel1 = tk.Label(root, text="This is label n.1", fg="yellow", bg="blue", font="helvetica 12 underline", width=20, height=1)
textlabel1.pack()

textlabel2 = tk.Label(root, text="This is label n.2", fg="white", bg="red", font="times 16 overstrike", width=20, height=1)
textlabel2.pack()

bitmaplabel1 = tk.Label(root, bitmap="question", fg="gray", bg="black")
bitmaplabel1.pack()

bitmaplabel2 = tk.Label(root, bitmap="error", fg="pink", bg="green")
bitmaplabel2.pack()

root.mainloop()
