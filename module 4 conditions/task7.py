hours = int(input('Введите кол-во отработанных часов: '))
credit_debt = int(input('Введите остаток по кредиту: '))
food_price = int(input('Введите стоимость еды: '))

salary = (200 * hours) / 2 ** 3 + hours

if salary >= (credit_debt + food_price): print('Часов хватает. Можно отдохнуть')
else: print('Часов не хватает. Придётся работать больше!')
    