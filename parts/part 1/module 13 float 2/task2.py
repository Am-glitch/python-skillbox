def maximum_of_two(number1, number2):
    return int((number1 + number2 + abs(number1 - number2)) / 2)

def maximum_of_three(number1, number2, number3):
    return maximum_of_two(number3, maximum_of_two(number1, number2))

n1 = int(input('Введите число 1: '))
n2 = int(input('Введите число 2: '))
n3 = int(input('Введите число 3: '))

print(maximum_of_three(n1, n2, n3))