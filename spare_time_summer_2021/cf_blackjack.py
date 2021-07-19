import keyboard
import time

time.sleep(3)

command = "+cf t 1\n"
command_2 = "+cf h 1\n"

for i in range(10):
    keyboard.write(command, 0.01)
    keyboard.write(command_2, 0.01)

