"""

"""

from tkinter import *


root = Tk()
root.title("Text")
root.geometry("640x480+200+200")
root.config(bg="light gray")

text = Text(root, height=5, width=30)
text.pack()

text.insert(END, "Write text here")

root.mainloop()
