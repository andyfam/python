# this example demonstrate how to use a function as parameter

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

# this example demonstrate how to return a function as result

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))