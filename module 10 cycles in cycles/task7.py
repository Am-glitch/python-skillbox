levels = int(input("Введите количество уровней пирамиды: "))

current_number = 1

for i in range(1, levels + 1):
    spaces = ' ' * (levels - i)
    numbers = ' '.join(str(current_number + 2 * j) for j in range(i))
    print(spaces + numbers)
    current_number += 2 * (i - 1)