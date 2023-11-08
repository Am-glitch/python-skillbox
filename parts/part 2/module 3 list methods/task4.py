guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while(True):
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    answer = input('Гость пришёл или ушёл? ')
    if answer == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    guest = input('Имя гостя: ')
    if answer == 'пришёл' and len(guests) <= 6:
        guests.append(guest)
        print(f'Привет, {guest}!')
    else: 
        print(f'Прости, {guest}, но мест нет.')
    if answer == 'ушёл':
        if guest in guests:
            guests.remove(guest)
            print(f'Пока, {guest}!')
        else: 
            print('Странно, его с нами и так нет')
    

          
