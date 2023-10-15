X = int(input('Сумма вклада: '))
Y = int(input('Прогнозируемая сумма: '))
P = int(input('Проценты: '))
years = 0

while True: 
    if X >= Y: 
        print(f'Понадобится {years} лет')
        break
    X += X * (P / 100)
    X = int(X)
    years += 1