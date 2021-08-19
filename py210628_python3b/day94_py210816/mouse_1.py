"""
Create a window
Display the coordinates of mouse cursor when you click the LB

Expected result:
clicked at (45, 60)
clicked at (104, 362)
"""

from tkinter import *


def handler(event):
    print(f"{event.x}, {event.y}")


root = Tk()
root.title("Event Handling")
root.geometry("640x480+200+200")
root.config(bg="#ddddff")

# test Left mouse button (LMB)
root.bind('<Button-1>', handler)

root.mainloop()
