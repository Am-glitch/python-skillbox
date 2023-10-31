a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
count = 0
sum = 0

for number in range(a, b + 1):
    if number % 3 == 0: 
        sum += number
        count += 1

print('Среднее арифметическое чисел, кратных 3: ', sum / count)