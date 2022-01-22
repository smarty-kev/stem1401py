import keyboard
import time

file = open("twentyonepilots.txt", "r")

content = file.read()

time.sleep(3)

keyboard.write(content, 0.5)