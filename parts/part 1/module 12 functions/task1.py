def summa_n(N):
    if N == 1:
        return 1
    else: 
        return N + summa_n(N - 1)

number = int(input('Введите число: '))
print(f'Я знаю, что сумма чисел от 1 до {number} равна {summa_n(number)}')