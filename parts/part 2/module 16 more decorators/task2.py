from typing import Optional, Callable
import functools

class App:
    def __init__(self) -> None:
        self.routes = {}

    def get(self, path: str) -> Optional[Callable]:
        return self.routes.get(path)

    def callback(self, path: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.routes[path] = func
            return func

        return decorator

app = App()

@app.callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
