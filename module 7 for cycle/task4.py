N = int(input('Введите кол-во человек в классе: '))
counter1 = 0
counter2 = 0

for puple in range(N):
    grade = int(input('Введите оценку: '))
    if grade == 3: counter1 += 1
    elif grade == 4: counter2 += 1

print(f'В классе {N - (counter1 + counter2)} отличников, {counter2} хорошистов, {counter1} трочеников')