hour = 1
tasks_counter = 0
phone_picked_up = False

while(hour <= 8):
    print(f'{hour}-й час')
    tasks_counter += int(input('Сколько задач решит Максим? '))
    state = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if (state == 1): phone_picked_up = True
    hour += 1

print('Рабочий день закончился. Всего выполнено задач: ', tasks_counter)
if (phone_picked_up): print('Нужно зайти в магазин.')