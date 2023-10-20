a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))

c = int(input('На какое число должно делиться? '))

numbers = [i for i in range(a, b + 1)]

target_numbers = [i for i in numbers if i % c == 0]

print(f'Среднее арифметическое чисел, делящихся на {c}: {sum(target_numbers) / len(target_numbers)}')