numbers = [int(x) for x in input('Введите три числа: ').split(' ')]
print(sorted(numbers))

tempArr = [numbers.count(i) for i in numbers]
print(max(tempArr))

