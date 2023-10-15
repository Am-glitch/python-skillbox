counter1 = 0
counter2 = 0
while(True):
    number = int(input('Введите число: '))
    if number == 0:
        print(f'Кол-во положительных чисел: {counter1}')
        print(f'Кол-во отрицательных чисел: {counter2}')
        break
    if number > 0: counter1 += 1
    else: counter2 += 1