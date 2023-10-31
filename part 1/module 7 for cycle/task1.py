count = 0
for people in range(10):
    client_number = int(input('Введите номер человека: '))
    if (client_number % 2 == 0 and client_number > 0): count += 1 

print('Должников: ', count)