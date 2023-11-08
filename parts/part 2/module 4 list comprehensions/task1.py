text = input('Введите текст: ')

vowel_letters = [letter for letter in text if letter.lower() in ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']]

print('Список гласных букв:', vowel_letters)
print('Длина списка:', len(vowel_letters))