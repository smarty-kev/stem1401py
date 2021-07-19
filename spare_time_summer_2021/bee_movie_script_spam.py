import keyboard
import time

file = open("bee_movie_script.txt", "r")

content = file.read()

time.sleep(3)

keyboard.write(content, 0.001); """
"""