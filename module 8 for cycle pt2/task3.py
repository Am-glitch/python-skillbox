reverse_timer = int(input('На сколько секунд ставите еду? '))

for time in range(reverse_timer, -1, -1):
    if time == 0: 
        print('Ваша еда готова, осторожно горячo!')
        break
    print(f'До полной готовности: {time}')
    state = int(input('Готовы забрать еду? '))
    if state == 1: 
        print(f'Ваша еда готова, можете забрать, секунд оставалось: {time}')
        break 
    
