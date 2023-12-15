def print_numbers_recursive(num):
    if num > 0:
        print_numbers_recursive(num - 1)
        print(num)

num = int(input('Введите число: '))
print_numbers_recursive(num)
