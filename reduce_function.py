import functools

# use reduce function to concatenate letters

letters = ["H", "E", "L", "L", "O"]

hello = functools.reduce(lambda x,y: x + y, letters)

print(hello)

# use reduce function to get the factorial

factorial = [5, 4, 3, 2, 1]

result = functools.reduce(lambda x,y: x * y, factorial)

print(result)