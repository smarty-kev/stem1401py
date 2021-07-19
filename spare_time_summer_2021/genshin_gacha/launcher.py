"""
genshin gacha system
By : Kevin Liu, macOS Sierra v10.12.6 (16G2136)
Started : 14 June 2021

Disclaimer:
this is for fun cuz i am very bored
"""

# modules
from tkinter import *
import time
import datetime


# functions
def start_game():
    interval = 0.01

    progress_label = Label(text="")
    start_B.destroy()
    progress_label.place(relx=0.4, rely=0.5)
    time.sleep(interval)
    for i in range(0, 21):
        if i != 21:
            progress_label.config(text=f"[{'◼' * (i - 1) + '>':20}]{5 * i}%")
            progress_label.update()
            time.sleep(interval)
        if i == 20:
            progress_label.config(text=f"[{'◼' * i:20}]{5 * i}%")
            progress_label.update()
            time.sleep(interval)
    launcher_window.destroy()
    with open("profile.txt", "r+") as data:
        content = data.readlines()
    data.close()
    data = open("profile.txt", "w")
    content[-2] = f"last login : {datetime.datetime.now()}\n"
    data.writelines(content)
    data.close()
    exec(open("main_program.py").read())


# open loading screen
launcher_window = Tk()
launcher_window.title("Genshin Launcher (fanmade)")
launcher_window.geometry("1087x722")

# background
bg = PhotoImage(file="genshin_loading_screen.png")
bg_img = Label(launcher_window, image=bg)
bg_img.place(x=-3, y=-3)

# start button
start_B = Button(text="Start", width=20, height=3, command=start_game)
start_B.place(relx=0.4, rely=0.5)

launcher_window.mainloop()
