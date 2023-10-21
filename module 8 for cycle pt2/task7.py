N = int(input('Введите кол-во элементов: '))

sum = 0
for n in range(N):
    sum += (-1) ** n * (1 / 2 ** n)

print(f'сумма равна: {sum}')