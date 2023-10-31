array = [1, 4, -3, 0, 10]

k = int(input('Сдвиг: '))
# 1 2 3 4 5 -> 5 1 2 3 4
print('Изначальный список:', array)
print('Сдвинутый список:', array[len(array) - k:] + array[:len(array) - k])