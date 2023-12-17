from typing import Callable
import functools

def check_permission(user_permission: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            required_permissions = ['admin']
            if user_permission in required_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")

        return wrapper

    return decorator

@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')

delete_site()
add_comment()
