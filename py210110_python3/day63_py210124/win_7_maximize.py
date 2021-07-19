"""
maximize
"""

import tkinter as tk
import time

root = tk.Tk()
root.title("Python GUI - Subtopic")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")

root.update()

time.sleep(3)

# maximize
try:
    root.attributes("-zoomed", 1)
except Exception as e:
    print(e)

root.state("zoomed")

def restore():
    print("restoring")
    root.state("normal")


btn1 = tk.Button(root, text="Restore", command=restore())

root.mainloop()