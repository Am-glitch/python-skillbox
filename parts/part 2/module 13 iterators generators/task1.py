from collections.abc import Iterable


class NumbersSquares:
    def __init__(self, count: int) -> None:
        self.count = count
        self.current = 0

    def __next__(self) -> int:
        self.current += 1
        if self.current > self.count:
            raise StopIteration
        return self.current ** 2
    
    def __iter__(self) -> Iterable[int]:
        return self 
    

def generate_numbers_squares(count: int) -> Iterable[int]:
    for number in range(1, count + 1):
        yield number ** 2


print(list(NumbersSquares(10)))
print(list(generate_numbers_squares(10)))
print(list(number ** 2 for number in range(1, 11)))