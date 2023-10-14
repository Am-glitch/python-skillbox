num1 = int(input('Введите 1-ое число: '))
num2 = int(input('Введите 2-ое число: '))

print((num1 % 10 + num2 % 10) + ((num1 % 100 - num1 % 10) + (num2 % 100 - num2 % 10)))