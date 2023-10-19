def inverse(number):
    digits = [int(digit) for digit in str(number)]
    print('Число наоборот:', ''.join(map(str, list(reversed(digits)))))

while(True):
    number = int(input('Введите число: '))
    if number == 0: 
        print('Программа завершена!')
        break

    inverse(number)