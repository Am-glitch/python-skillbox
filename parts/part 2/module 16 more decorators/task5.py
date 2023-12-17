from typing import Type

def singleton(cls: Type) -> Type:
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Example:
    pass

my_obj: Example = Example()
my_another_obj: Example = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
