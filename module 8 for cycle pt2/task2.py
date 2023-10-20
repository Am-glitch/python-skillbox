people_amount = int(input('Введите кол-во должников: '))
summary = 0
for order in range(0, people_amount + 1, 5):
    print(f'Должник с номером {order}')
    summary += int(input('Сколько должен? '))

print(f'Общая сумма долга: {summary}')
