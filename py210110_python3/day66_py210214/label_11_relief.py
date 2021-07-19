"""
relief="value"
value = flat, groove, raised, ridge, solid, sunken
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Relief")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


label1 = tk.Label(root, text="Text Label", relief="flat", padx=20, pady=15)
label1.pack()

label2 = tk.Label(root, text="Text Label", relief="groove", padx=20, pady=15)
label2.pack()

label3 = tk.Label(root, text="Text Label", relief="raised", padx=20, pady=15)
label3.pack()

label4 = tk.Label(root, text="Text Label", relief="ridge", padx=20, pady=15)
label1.pack()

label5 = tk.Label(root, text="Text Label", relief="solid", padx=20, pady=15)
label5.pack()

label6 = tk.Label(root, text="Text Label", relief="sunken", padx=20, pady=15)
label6.pack()


root.mainloop()