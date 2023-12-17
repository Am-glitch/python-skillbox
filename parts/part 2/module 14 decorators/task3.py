from datetime import datetime
import functools
from typing import Callable


def log(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print('Вызвана функция: ', func.__name__)
        print('Документация:')
        print(func.__doc__)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            message = f'{datetime.utcnow()}: {func.__name__} выбросила исключение: {repr(e)}'
            print(message)
            with open('function_errors.log', 'a', encoding='utf-8') as log:
                log.write(message + '\n')

    return wrapped_func


@log
def test():
    print('<Тут что-то происходит...>')


@log
def test_with_error():
    raise ValueError('Просто исключение')


test()
test_with_error()