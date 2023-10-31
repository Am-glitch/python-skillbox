dollar_cost = 60.87
euro_cost = 1.25 * dollar_cost

price_in_euro = int(input('Введите стоимость в евро: '))

print(f'Стоимость в рублях: {round(price_in_euro * euro_cost, 2)}')