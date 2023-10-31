start = int(input('Введите начало отрезка: '))
stop = int(input('Введите конец отрезка: '))

step = int(input('Введите шаг: '))

for x in range(start, stop + 1, step):
    y = x**3 + 2 * x ** 2 - 4 * x + 1
    print(f'В точке {x} функция равна {y}')