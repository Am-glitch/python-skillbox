rows = int(input('Введите кол-во рядов: '))
seats_in_row = int(input('Введите кол-во сидений в ряду: '))
gap = int(input('Введите кол-во метров между рядами: '))

for row in range(rows):
    print('=' * seats_in_row, '' , '*' * gap, '', '=' * seats_in_row)