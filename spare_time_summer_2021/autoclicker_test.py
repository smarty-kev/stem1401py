from pynput.mouse import Button, Controller
import time

time.sleep(3)

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release
while True:
    mouse.press(Button.left)
    mouse.release(Button.left)


# DO NOT RUN THIS FILE
