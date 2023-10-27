n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))

max_number = (n1 + n2 - abs(n2 - n1)) / 2 + abs(n2 - n1)
print(f'Наибольшее число: {int(max_number)}')
