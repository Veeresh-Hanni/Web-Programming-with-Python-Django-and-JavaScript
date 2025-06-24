def hi():
    print("Hi there!")

def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0


def square(n):
    return  n * n


def squares(*args):    
    return args[0] * args[0] if args else None

def cube(n):
    return n * n * n



# Calling the functions to demonstrate their functionality
if __name__ == "__main__":
    hi()
    greet("Alice")
    print(f"Sum: {add(5, 3)}")
    print(f"Product: {multiply(4, 2)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 5 odd? {is_odd(5)}")
    print(f"Square of 3: {square(3)}")
    print(f"Cube of 2: {cube(2)}")