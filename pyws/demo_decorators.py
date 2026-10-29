from functools import wraps
class Demo:
    def __init__(self):
        ...

    @property
    def name(self):
        ...

    @classmethod
    def f(cls):
        ...


def say_hello():
    print("Hello, how are you?")


# 1. Functions as objects
greet = say_hello
# greet()


# 2. Functions as arguments
def my_simple_decorator(func):
    print("Decorating the function")
    func()

# my_simple_decorator(say_hello)


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling the decorated function")
        result = func(*args, **kwargs)
        print("After calling the decorated function")
        return result
    return wrapper


# say_hello = my_decorator(say_hello)
# say_hello()

@my_decorator
def say_hello(name: str):
    print(f"Hello {name}, how are you?")

# say_hello("Marco")

def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(38)