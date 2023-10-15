target_number = 7
attempts = 0
while(True):
    number = int(input('Введите число: '))
    if (number == target_number):
        print('Вы угадали! Число попыток: ', attempts)
        break
    print('Число меньше, чем нужно. Попробуйте ещё раз!' if number < target_number 
          else 'Число больше, чем нужно. Попробуйте ещё раз!')
    attempts += 1