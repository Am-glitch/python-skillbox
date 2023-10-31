height = int(input("Введите высоту пирамиды: "))

for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    hashes = '#' * (2 * i - 1)
    print(spaces + hashes)