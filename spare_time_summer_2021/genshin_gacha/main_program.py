"""
genshin gacha system
By : Kevin Liu, macOS Sierra v10.12.6 (16G2136)
Started : 14 June 2021

Disclaimer:
this is for fun cuz i am very bored

backup
name : ""
balance : "0"
inventory :
last login :

"""

# modules
from tkinter import *
import random
import time
import datetime


# functions
datetime_format = "%Y-%m-%d %H:%M:%S.%f"


def daily_primogems():
    global datetime, datetime_format
    with open("profile.txt", "r+") as data:
        profile = data.readlines()
        print(profile)
        if profile[-1] != "last primogems claim :":
            last_login_str = profile[-2]; last_login_str = last_login_str.strip()
            last_login_str = last_login_str.replace('last login : ', '')
            last_claim_str = profile[-1]; last_claim_str = last_claim_str.strip()
            last_claim_str = last_claim_str.replace('last primogems claim :', '')
            last_login = datetime.datetime.strptime(last_login_str, datetime_format)
            try:
                last_claim = datetime.datetime.strptime(last_claim_str, datetime_format)
            except Exception:
                last_claim = last_login
            uptime = last_claim - last_login
        else:
            uptime = 0
            new_balance = f'balance : "{1000}"\n'; profile[1] = new_balance
            last_claim_str = profile[-2]
            last_claim_str = last_claim_str.strip()
            last_claim_str = last_claim_str.replace('last login :', '')
            last_claim_str = last_claim_str.replace(' ', '')
            profile[-1] = f"last primogems claim :{last_claim_str}"
            print(profile)
        if uptime > 1:
            balance = profile[2]; balance = balance.strip(); balance = balance.replace('balance : ', '')
            balance = balance.replace('"', ''); balance = int(balance) + 100
            new_balance = f'balance : "{balance}"\n'
            profile[1] = new_balance
            profile[-1] = last_login_str
        data.truncate(0)
        print(profile)
        data.writelines(profile)
        data.close()


def login():
    global main_window, daily_primogems
    time.sleep(1)
    with open("profile.txt", "r+") as data:
        file_data = data.readlines()
        # print(file_data)
        name = file_data[0]
        name = name.strip()
        name = name.replace('name : ', '')
        name = name.replace('"', '')

        balance = file_data[1]
        balance = balance.strip()
        balance = balance.replace('balance : ', '')
        balance = balance.replace('"', '')

    welcome_label = Label(text=f"Welcome back {name}!")
    welcome_label.grid()

    primogems_label = Label(text=f"Your balance, traveler : {balance} primogems")
    if balance == "0":
        primogems_label.config(text="Sad, the traveler is broke. (°o°)")
    primogems_label.grid()
    main_window.update()
    data.close()
    daily_primogems()


def get_username():
    global entry_username, content, time, prompt, label_username, entry_username, confirm_B, login, datetime
    data = open("profile.txt", "w")
    new_name = f'name : "{entry_username.get()}"\n'
    content[0] = new_name
    time.sleep(1)
    prompt.destroy()
    label_username.destroy()
    entry_username.destroy()
    confirm_B.destroy()
    # daily primogems
    data.writelines(content)
    data.close()
    login()


# game window
main_window = Tk()
main_window.title("Genshin Gacha (fanmade)")
main_window.geometry("600x200")


# check if account was already created
not_created = False

welcome_msg = "Welcome Traveler! This is the world of Teyvat, where your adventure will now unfold!"
with open("profile.txt", "r+") as file:
    content = file.readlines()
    if content[0] == 'name : ""\n':
        prompt = Label(main_window, text=welcome_msg)
        prompt.grid(columnspan=2, padx=20, pady=10)
        label_username = Label(text="The traveler's name? ")
        label_username.grid(column=0)
        string = StringVar()
        entry_username = Entry(textvariable=string)
        entry_username.grid(column=1, row=1, pady=10)
        confirm_B = Button(text="Confirm", command=get_username, width=10, height=2)
        confirm_B.grid(columnspan=2)
        file.close()
    else:
        file.close()
        login()


main_window.mainloop()
