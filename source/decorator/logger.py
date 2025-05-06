from functools import wraps
from typing import Callable


def logger(func: Callable) -> Callable:
    @wraps(func)  # @wraps behoudt de metadata van de functie
    def wrapper(*args, **kwargs):
        print(func.__doc__)
        print(f"calling function {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
