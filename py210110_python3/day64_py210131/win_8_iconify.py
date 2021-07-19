"""
root.iconify()
"""

import time
import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Subtopic")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")

root.update()
time.sleep(2)

# case 1
root.iconify()

root.mainloop()
