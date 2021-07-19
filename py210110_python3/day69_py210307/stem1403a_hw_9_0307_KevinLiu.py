"""
Date: 2021-03-08
1. Write a GUI program of clock
Requirements:
(Function)
Show current time in the pattern of HH:mm:ss.aaa
i.e.
10:12:45.369
(UI)
Display a title, main area for clock, and footer for the date
Due date: by the end of next Friday
Hint:
import datetime
strftime
"""

# tkinter module
from tkinter import *
from tkinter.ttk import Separator
import datetime


# function
def run_clock():
    current_time.configure(text=datetime.datetime.now().strftime("%H:%M:%S.%f")[:12])
    current_time.after(1, run_clock)


# widget
root = Tk()
root.title('Python GUI - pack fill')
w_width = 640; w_height = 380
sw = root.winfo_screenwidth(); sh = root.winfo_screenheight()
top_left_x = int(sw/2 - w_width/2); top_left_y = int(sh/2 - w_height/2)
root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")

# header
header = Label(text="System Time", fg="Black", font=("Helvetica", 28))
header.pack(padx=15, pady=15)

# separator 1
sep = Separator(root, orient=HORIZONTAL)
sep.pack(fill=X)

# current time label
time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
current_time = Label(text=time, bg="green", fg="White", font=("Helvetica", 36), width=15, height=5)
current_time.pack(padx=15, pady=15)

# separator 2
sep2 = Separator(root, orient=HORIZONTAL)
sep2.pack(fill=X)

# footer
footer = Label(text="Version 1, Kevin Liu, 12 March 2021", fg="Black", font=("Helvetica", 28))
footer.pack(padx=15, pady=15)

# main program
run_clock()

root.mainloop()
