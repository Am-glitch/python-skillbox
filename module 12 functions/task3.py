def sumDigits(n):
    digits = [int(num) for num in str(n)]
    print('сумма цифр числа:',sum(digits))

def max_digit(n):
    digits = [int(num) for num in str(n)]
    print('максимальная цифра числа:', max(sorted(digits)))

def min_digit(n):
    digits = [int(num) for num in str(n)]
    print('минимальная цифра числа:', min(sorted(digits)))

def calculator():
    n = int(input('Введите число: '))
    operation = int(input('Выберите операцию: \n1-сумма цифр числа\n2-максимальная цифра числа\n3-минимальная цифра числа\n'))
    if operation == 1: 
        sumDigits(n)
    elif operation == 2:
        max_digit(n)
    elif operation == 3:
        min_digit(n)
    else:
        print('Нет такой операции')

while True:
    calculator()