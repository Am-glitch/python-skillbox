N = int(input('Введите число: '))

array = [n for n in range(1, N + 1) if n % 2 != 0]

print("Список из нечётных чисел от одного до N:", array)