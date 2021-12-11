"""
genshin gacha system
By : Kevin Liu, macOS Sierra v10.12.6 (16G2136)
Started : 14 June 2021

Disclaimer:
this is for fun cuz i am very bored
"""

# modules
from tkinter import *
import time, datetime, os


# functions
class Window:
    def __init__(self, name, title, geometry, bg=None):
        self.name = name
        self.title = title
        self.geometry = geometry
        self.bg = bg
        self.bg = PhotoImage(file=bg)
        bg_img = Label(self.name, image=bg)
        bg_img.place(x=-3, y=-3)

def create_account():
    # create a password file
    file_name = 'credentials.txt'
    if not os.path.isfile(file_name):
        f = open(file_name, 'w')

    # account creation
    new_user = False
    if os.stat(file_name).st_size == 0:
        new_user = True

    if new_user:
        username = input("Please enter your username: ")
        password = input("Please enter a strong password: ")
        date_of_birth = input("Please enter your birthday: ")
        eula = "Please accept the terms and conditions (input 'yes'). For more information, visit 'info.com': "
        # end user licence agreement
        agreement = input(eula)
        if agreement == 'yes':
            file = open(file_name, 'w')
            content = f"{username} {password} {date_of_birth}"
            file.write(content)
            print("Nice, you have successfully created an account.")
            print("\n\n\n")
        else:
            print("Please try again and accept the terms and conditions of use and policy policies. Refresh the page. ")


def start_game(window):
    window.destroy()


def open_launcher():
    launcher_window = Tk()
    launcher_window.title("Genshin Launcher (fanmade)")
    launcher_window.geometry("900x420")

    # background
    bg = PhotoImage(file="genshin_loading_screen.png")
    bg_img = Label(launcher_window, image=bg)
    bg_img.place(x=-3, y=-3)

    # start button
    start_B = Button(text="Start", width=20, height=3, command=lambda: start_game(launcher_window))
    start_B.place(relx=0.4, rely=0.5)

    launcher_window.mainloop()


# main program
create_account()  # will only execute if new user (no credentials.txt file detected)
title = "Genshin Launcher (fanmade)"
geometry = "900x420"
window_launcher = Window(name, title, geometry, bg="genshin_loading_screen.png")
open_launcher()
