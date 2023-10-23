N = int(input('Введите число N: '))

for row in range(1, N + 1):
    print(' '.join([str(row)] * row))

