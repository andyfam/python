import threading
import time

def timer():
    count = 0

    print()
    print()
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:" + str(count) + " seconds!")

x = threading.Thread(target=timer, daemon=True)
x.start()

input("Do you want to exit?")