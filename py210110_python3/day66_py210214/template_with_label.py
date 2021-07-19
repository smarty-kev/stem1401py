"""

"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Subtopic")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


label1 = tk.Label(root, text="Text Label")

label1.pack()

root.mainloop()