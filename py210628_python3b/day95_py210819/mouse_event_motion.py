"""
mouse event
<Motion>
"""

from tkinter import *


def handler(event):
    print(f"clicked at ({event.x}, {event.y})")

    x = event.x
    y = event.y
    textvar = "Mouse location is x: {}, y: {}".format(x, y)
    var.set(textvar)


root = Tk()
root.title("Mouse Event Motion")
root.geometry("640x480+200+200")
root.config(bg="#ddddff")

# init pos
x = 0
y = 0

# label of text (x, y)

var = StringVar()
text = "Mouse location is x: {}, y: {}".format(x, y)
var.set(text)

label_coord = Label(root, textvariable=var, bg="#ddddff")
label_coord.pack(anchor=S, side=RIGHT)


root.bind("<Motion>", handler)

root.mainloop()
