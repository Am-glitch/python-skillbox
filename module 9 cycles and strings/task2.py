text = input('Введите текст: ')
index = 0
i = 1
for symbol in text: 
    if symbol == '*': 
        index = i
        break
    i += 1

print(f'Символ «*» стоит на позиции {index}')