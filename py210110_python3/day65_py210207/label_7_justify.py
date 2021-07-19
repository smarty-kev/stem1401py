"""
font in a label
font = "Helvetica 20 bold italic"
font = ("Times", 16, "normal", "roman")
"""
import tkinter as tk
# from tkinter import *
root = tk.Tk()
root.title('Python GUI - label')
winw= 800
winh= 600
posx=300
posy=200
root.geometry(f'{winw}x{winh}+{posx}+{posy}')
root.config(bg='#ddff77')
# create a label
mytext = 'My Text Label font'
label1 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='red', fg='#ffffff',
                  font = 'Helvetica 20 italic underline',
                  justify='left',wraplength=190)
label1.pack(side=tk.RIGHT)
# create a label
label2 = tk.Label(root, text=mytext,
                  width=30, height=3,
                  bg='blue', fg='#ffffff',
                  font = 'Helvetica 24 bold overstrike',
                  justify='right',wraplength=190)
label2.pack()
# create a label
label3 = tk.Label(root, text=mytext,
                  width=30, height=5,
                  bg='red', fg='gold',
                  font='"Segoe UI" 18 bold underline overstrike',
                  justify='center',wraplength=190)
label3.pack()
root.mainloop()