a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)

count_5 = a.count(5)
print('Количество цифр 5 при первом объединении:',count_5)

a = [i for i in a if i != 5]
a.extend(c)

count_3 = a.count(3)
print('Количество цифр 3 при втором объединении:', count_3)

print('Итоговый список:', a)
