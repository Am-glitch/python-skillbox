string = input('Введите строку: ')
result = ''
temp_count = 1
for i_symbol in range(1, len(string)):
    if string[i_symbol] == string[i_symbol - 1]:
        temp_count += 1
    else:
        result += string[i_symbol - 1] + str(temp_count)
        temp_count = 1

result += string[-1] + str(temp_count)

print(f'Закодированная строка: {result}')