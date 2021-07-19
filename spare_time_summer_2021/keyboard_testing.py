import keyboard

# keyboard.write("Python Programming is always fun!", delay=0.1)

# keyboard.press("left click")

# take screenshot
# keyboard.send("command+shift+3")


# record all keyboard clicks until esc is clicked
events = keyboard.record('esc')
# play these events
keyboard.play(events)

