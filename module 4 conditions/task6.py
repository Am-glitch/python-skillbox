player_cube = int(input('Кубик игрока: '))
owner_cube = int(input('Кубик владельца: '))

if player_cube >= owner_cube: 
    print(f'Разность: {player_cube - owner_cube} \nИгрок платит')
else: print(f'Сумма: {player_cube + owner_cube} \nВладелец платит')