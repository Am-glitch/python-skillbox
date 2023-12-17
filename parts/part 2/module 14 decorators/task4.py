import functools
import random
from typing import Callable 

def counter(func: Callable, calls_count = dict()) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        calls_count[func] = calls_count.get(func, 0) + 1
        print(f'Вызов функции {func.__name__} - {calls_count[func]}')
        return func(*args, **kwargs)
    return wrapped_func

@counter 
def test1():
    pass 

@counter
def test2(): 
    pass 

for i in range(10):
    func_to_execute = random.choice([test1, test2])
    func_to_execute()