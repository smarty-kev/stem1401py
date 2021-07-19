"""
set resizable
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Subtopic")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")

# resizable
root.resizable(False, False)

root.resizable(1, 0)

root.resizable(0, 1)

root.mainloop()