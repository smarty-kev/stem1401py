"""
Keyboard Event

References
https://cn.pythonexample.org/gui/how-to-handle-keyboard-events-with-tkinter-in-python/
"""

#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


# process press keyboard event
def handleKeyEvent(event):
    label1["text"] = "The key You pressed is \t" + event.keysym + " \n"
    label1["text"] += "And the keycode is \t\t" + str(event.keycode)


# create the main window
root = Tk()
root.geometry("640x480+300+300")
frame = Frame(root, relief=RAISED, borderwidth=1, width=480, height=320)

# link keyboard event to main window
eventType = ["Key", "Control-Up", "Return", "Escape", "F1", "F2", "F3", "F4", "F5",
             "F6", "F7", "F8", "F9", "F10", "F11", "F12", "Num_Lock", "Scroll_Lock",
             "Caps_Lock", "Print", "Insert", "Delete", "Pause", "Prior", "Next", "BackSpace",
             "Tab", "Cancel", "Control_L", "Alt_L", "Shift_L", "End", "Home", "Up", "Down",
             "Left", "Right"]

for type in eventType:
    root.bind("<" + type + ">", handleKeyEvent)

label1 = Label(frame, text="No keyboard pressed now",
               foreground="#000fff", background="#ddddff",
               font=(None, 14))
label1.place(x=15, y=18)

# set location
frame.pack(side=TOP)

# event loop
root.mainloop()