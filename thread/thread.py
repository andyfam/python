import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("Eating breakfast!")

def drink_coffe():
    time.sleep(4)
    print("Drinking coffee!")

def study():
    time.sleep(5)
    print("Studying!")

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffe, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# we can use join() to make main thread running after these three threads are done
# x.join()
# y.join()
# z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
