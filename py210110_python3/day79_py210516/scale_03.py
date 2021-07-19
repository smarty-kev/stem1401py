"""
Scale
usage of Scale
binding a variable
change a value via variable
get a value
set a value
"""
from tkinter import *
def bgUpdate(source):
    """change background color"""
    red = rSlider.get()
    green = gSlider.get()
    blue = bSlider.get()
    # convert to HEX
    myColor = f"#{red:02x}{green:02x}{blue:02x}"
    root.config(bg=myColor)
root = Tk()
root.title("Python GUI - Scale")
root.geometry("360x240")
root.config(bg="#ddddff")
rSlider = Scale(root, from_=0, to=255, label="R", tickinterval = 10,\
                resolution=1, troughcolor="red", command=bgUpdate)
gSlider = Scale(root, from_=0, to=255, label="G", \
                resolution=5, troughcolor="green", command=bgUpdate)
bSlider = Scale(root, from_=0, to=255, label="B", \
                resolution=1, troughcolor="blue", command=bgUpdate)
rSlider.pack(anchor=S, side=LEFT)
gSlider.pack(anchor=S, side=LEFT)
bSlider.pack(anchor=S, side=LEFT)
root.mainloop()