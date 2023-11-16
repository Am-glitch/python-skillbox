pairs_amount = int(input('Введите количество пар слов: '))
pairs_dict = dict()

for i_pair in range(pairs_amount):
    pair = input(f'{i_pair + 1}-я пара: ')

    pairs_dict[pair.split(' - ')[0]] = pair.split(' - ')[1]

while True:
    found = False
    word = input('Введите слово: ')
    for word in pairs_dict.keys():
        if (word.lower() == word.lower()):
            print(f'Синоним: {pairs_dict[word]}') 
            found = True
            break
        elif (pairs_dict[word].lower() == word.lower()):
            print(f'Синоним: {word}')
            found = True
            break

    if found: break
    print('Такого слова в словаре нет.')   
        