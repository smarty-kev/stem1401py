"""
my first GUI program
Tkinter

Widget
Create a title for main window
"""

# import tkinter
from tkinter import *

try:
    root = Tk()
    root.title("Python GUI - My first GUI App")
    # root.geometry("640x480")
    # root.geometry("800X600")
    # root.geometry("800x600")

    # 16:9 ratio
    root.geometry("1600x900")
    root.mainloop()

except TclError as te:
    print(te)
