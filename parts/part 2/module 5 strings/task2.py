string = input('Введите строку: ')

max_word = max([word for word in string.split(' ')], key = lambda x: len(x))
print(f'Самая длинное слово: {max_word}')
print(f'Длина этого слова: {len(max_word)} символов.')