import os

src = "test.txt"
dst = "move.txt"

try:
    if os.path.exists(dst):
        print(dst + " is already exists!")
    else:
        os.replace(src, dst)
        print(src + " was moved to " + dst)
except FileNotFoundError:
    print(src + " could not be found!")