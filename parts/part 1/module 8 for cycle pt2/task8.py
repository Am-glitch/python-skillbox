x = int(input("Введите количество мальчиков: "))
y = int(input("Введите количество девочек: "))

if abs(x - y) > 1:
    print("Нет решения")

boys = min(x, y)
girls = min(x, y)
seating = ''

for i in range(boys + girls):
    if i % 2 == 0:
        seating += 'B'
        boys -= 1
    else:
        seating += 'G'
        girls -= 1

print(seating)











