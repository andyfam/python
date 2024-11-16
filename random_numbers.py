import random

# random int
x = random.randint(1, 6)
print(x)

# random float
y = random.random();
print(y)

# ramdom choice an element in a list
myList = ['Rock', 'Paper', 'Scissor']
z = random.choice(myList)
print(z)

# shuffle a list
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)
