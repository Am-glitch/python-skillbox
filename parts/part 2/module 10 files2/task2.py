import random 


total = 777

try:
    with open('test/out_file.txt', 'w') as out_file:
        while total > 0:
            number = int(input('Введите число: '))
            if random.randint(1, 13) == 13:
                raise Exception
            total -= number
            out_file.write(f'{str(number)}\n')
except Exception:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')