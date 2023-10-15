first_price = int(input('Введите стоимость товара: '))
second_price = int(input('Введите стоимость товара: '))
third_price = int(input('Введите стоимость товара: '))

summary = first_price + second_price + third_price

if summary >= 10000: 
        print(summary - summary * 0.1)
else: 
        print(summary)