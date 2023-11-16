goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}
store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
}

formatted_goods_dict = dict()

for good in goods.keys():
    quantity = 0
    price = 0

    for i_info in range(len(store[goods[good]])):
        quantity += store[goods[good]][i_info]['quantity']
        price += store[goods[good]][i_info]['quantity'] * store[goods[good]][i_info]['price']
    
    formatted_goods_dict[good] = {
        'quantity': quantity,
        'price': price
    }

for good in formatted_goods_dict.keys():
    quantity = formatted_goods_dict[good]['quantity']
    price = formatted_goods_dict[good]['price']
    print(f'{good} — {quantity} штук, стоимость {price} рубля.')
  