start_x = 8
start_y = 10

while(True):
    input_command = input(f'Марсоход находится на позиции {start_x},{start_y}, введите команду: ')
    if input_command == 'W' and start_y < 20:
        start_y += 1
    elif input_command == 'S' and start_y > 0:
        start_y -= 1
    elif input_command == 'D' and start_x < 15:
        start_x += 1
    elif input_command == 'A' and start_x > 0:
        start_x -= 1

    