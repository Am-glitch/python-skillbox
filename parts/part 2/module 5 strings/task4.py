string = input('Введите строку: ')

result = ' '.join(word.capitalize() for word in string.split())

print(result)