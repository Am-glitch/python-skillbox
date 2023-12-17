import time
from typing import Callable, Any, Tuple

class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args: Tuple[Any], **kwargs: dict) -> Any:
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        print(f"Результат: {result}")
        print(f"Время выполнения: {execution_time} секунд")

        return result

@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result

result = complex_algorithm(10, 50)
