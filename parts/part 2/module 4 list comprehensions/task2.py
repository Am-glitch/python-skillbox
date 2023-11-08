N = int(input('Введите длину списка: '))
sequence = [number % 5 if number % 2 != 0 else 1 for number in range(N)]
print('Результат', sequence)