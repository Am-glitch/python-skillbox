def sum_custom(*args):
    total = 0

    for arg in args:
        if isinstance(arg, list):
            total += sum_custom(*arg)
        else:
            total += arg

    return total

result1 = sum_custom([[1, 2, [3]], [1], 3])
print(f"Ответ в консоли: {result1}")

result2 = sum_custom(1, 2, 3, 4, 5)
print(f"Ответ в консоли: {result2}")
