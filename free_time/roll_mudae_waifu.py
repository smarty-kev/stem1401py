import keyboard
import time

time.sleep(3)

command = "$wa\n"
command_2 = "$Wa\n"

for i in range(5):
    keyboard.write(command, 0.01)
    keyboard.write(command_2, 0.01)

