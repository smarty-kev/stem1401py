"""
refreshing

root.update
"""


import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Subtopic")

winw = 800
winh = 450
posx = 300
posy = 200

root.geometry(f"{winw}x{winh}+{posx}+{posy}")


w = root.winfo_screenwidth()
h = root.winfo_screenheight()
print(w, h)

# refreshing
root.update()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
print(w, h)


root.mainloop()