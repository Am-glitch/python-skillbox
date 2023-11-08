shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
count = 0
total_price = 0

for i_item in range(len(shop)):
    if shop[i_item][0] == detail: 
        count += 1
        total_price += shop[i_item][1]
    
print('Количество деталей:', count)
print('Общая стоимость:', total_price)