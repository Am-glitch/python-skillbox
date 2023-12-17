import functools
import time
from collections.abc import Callable


def wait_timer(time_to_wait: float):
    def wait(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            time.sleep(time_to_wait)
            return func(*args, **kwargs)
        return wrapped_func
    return wait

    
@wait_timer(5)
def test():
    return 'test'

print(test())