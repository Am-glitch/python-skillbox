def reverse_number(number):
    reversed_number = ''
    for symbol in str(number): 
        reversed_number = symbol + reversed_number
    return int(reversed_number)

n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))

reversed_n1 = reverse_number(n1)
reversed_n2 = reverse_number(n2)

print('Первое число наоборот:', reversed_n1)
print('Второе число наоборот:', reversed_n2)
print('Сумма:', reversed_n1 + reversed_n2)
print('Сумма наоборот:', n1 + n2)

