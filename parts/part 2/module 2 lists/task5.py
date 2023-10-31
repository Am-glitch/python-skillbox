amount = int(input('Количество контейнеров: '))
weights = []

for container in range(amount):
    while(True):
        weight = int(input('Введите вес контейнера: '))
        if(weight <= 200): 
            weights.append(weight)
            break
        else:
            print('Вес контейнера не может превышать 200 кг.')
    

last_container = int(input('Введите вес нового контейнера: '))
index = len(weights) + 1

for container in range(len(weights)):
    if weights[container] == last_container: 
        index = container + 2

print('Номер, который получит новый контейнер:', index)