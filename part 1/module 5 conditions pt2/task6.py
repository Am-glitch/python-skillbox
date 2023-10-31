flat_price = int(input('Введите стоимость квартиры (в млн.): '))
flat_area = int(input('Введите площадь квартиры: '))

if flat_area >= 100 and flat_price <= 10:
    print(f'Квартира площадью {flat_area} и стоимостью {flat_price} млн. подходит')
elif (80 <= flat_area <= 100) and flat_price <= 7: 
    print(f'Квартира площадью {flat_area} и стоимостью {flat_price} млн. подходит')
else: print('Не нашлась подходящая')
