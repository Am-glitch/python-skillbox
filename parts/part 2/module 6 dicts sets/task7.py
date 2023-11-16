array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

set1 = set(array_1)
set2 = set(array_2)
set3 = set(array_3)

print('Задача 1: ')
print('Решение без множеств:', [element for element in array_1 if element in array_2 and element in array_3])
print('Решение с множествами:', set1 & set2 & set3)

print('Задача 2: ')
print('Решение без множеств:', [element for element in array_1 if element not in array_2 and element not in array_3])
print('Решение с множествами:', set1 - set2 - set3)