import math

N = int(input('Введите кол-во чисел: '))

for i in range(N):
    x = float(input('Введите число: '))
    if x > 0: 
        x = math.ceil(x)
        print(f'x = {x} \n{math.log(x)}')
    else: 
        x = math.floor(x)
        print(f'x = {x} \n{math.exp(x)}')
