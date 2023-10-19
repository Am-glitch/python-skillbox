def gcd(a, b):
    while b:
        a, b = b, a % b
    print('Наибольший общий делитель:', a)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

gcd(a, b)

