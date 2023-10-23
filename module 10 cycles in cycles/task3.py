width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))


for i in range(height):
    if i == 0 or i == height - 1:
        print('-' * width)
    else:
        print('|' + ' ' * (width - 2) + '|')




