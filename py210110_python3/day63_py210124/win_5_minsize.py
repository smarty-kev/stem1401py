"""
set a minimum size to expand

minsize != minimize
root.minsize()
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Subtopic")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")

# case 1.
# root.minsize()

# case 2.
root.minsize(300, 200)

root.mainloop()