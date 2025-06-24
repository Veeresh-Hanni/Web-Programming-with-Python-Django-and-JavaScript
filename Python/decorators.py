def announce(f):
    def wrapper(*args, **kwargs):
        print(f"\nCalling function '{f.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        f(*args, **kwargs)
        print(f"Function '{f.__name__}' has been decorated with 'announce'.")
    return wrapper


@announce
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")