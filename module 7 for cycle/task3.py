n = int(input('Введите число: '))
summ = 1

for number in range(1, n + 1):
    summ *= number
print(f'Факториал числа {n} - {summ}')