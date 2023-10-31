salary = 0
for month in range(12):
    salary += int(input('Введите зарплату: '))
print('Средняя зп за год: ', salary / 12)