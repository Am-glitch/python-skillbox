def create_frequency_dict(text):
    temp_dict = dict()
    for sym in text:
        if sym in temp_dict:
            temp_dict[sym] += 1
        else:
            temp_dict[sym] = 1

    return temp_dict

text = input('Введите текст: ')

frequency_dict = create_frequency_dict(text)
print(frequency_dict)

inverted_dict = dict()

for frequency in sorted(frequency_dict.values()):
    symbols_arr = []

    for sym in frequency_dict:
        if frequency_dict[sym] == frequency:
            symbols_arr.append(sym)

    inverted_dict[frequency] = symbols_arr

print('Инвертированный словарь частот: ')
print(inverted_dict)



# print('Оригинальный словарь частот: ')



# print('Инвертированный словарь частот: ')