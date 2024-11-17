path = "test.txt"

try:
    with open(path) as file:
        print(file.read())
except FileNotFoundError:
    print("File can not be found!")
