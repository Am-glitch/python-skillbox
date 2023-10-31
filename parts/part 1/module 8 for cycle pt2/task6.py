import math

educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))

debt = 0
prices = expenses

for month in range(1, 11):
    if month > 1: 
        prices += (0.03 * prices)
    debt += prices - educational_grant
    print(f'{month}.месяц траты {prices} не хватает {debt}')

print(f'Нужно попросить у родителей {"{:.2f}".format(debt)} рублей')