import functools 
from typing import Callable, Iterator 


def cache_func(func: Callable) -> Callable:
    values_dict = dict()
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print(values_dict)
        if args not in values_dict:
            values_dict[args] = func(*args, **kwargs)
        return values_dict[args]

    return wrapped_func

@cache_func
def fibonacci(count: int) -> Iterator[int]:
    if count <= 1:
        return count
    else:
        return fibonacci(count - 1) + fibonacci(count - 2)


print(fibonacci(10))

