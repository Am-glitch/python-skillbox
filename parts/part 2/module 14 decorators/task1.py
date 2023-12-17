import functools
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        input('Как дела?')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapped_func


@how_are_you
def test():
    print('test!')

test()