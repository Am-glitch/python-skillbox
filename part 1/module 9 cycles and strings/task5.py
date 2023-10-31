longest_word = max([word for word in input('Введите текст: ').split(' ')], key = lambda x: len(x))

print(f'Самое длинное слово {longest_word}, букв: {len(longest_word)}')