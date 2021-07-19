"""
set to topmost

root.attributes("-topmost, True)
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Subtopic")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")

# set topmost

root.attributes("-topmost", 1)
root.wm_attributes("-topmost", True)

root.mainloop()