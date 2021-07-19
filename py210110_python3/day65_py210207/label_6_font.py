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


label1 = tk.Label(root, text="normal text", font=("Times", 18, "bold", "underline"))

label1.pack()

label2 = tk.Label(root, text="small text", font="helvetica 12 italic overstrike")

label2.pack()

label3 = tk.Label(root, text="small text", font='"Arial Narrow" 16 italic')

label3.pack()

root.mainloop()
