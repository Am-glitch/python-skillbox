word = input('Введите слово: ')
is_palendrome = False

for i in range(int(len(word) / 2)):
    if word[i] != word[len(word) - i - 1]:
        print('Нет, это не палиндром!')
        break
    is_palendrome = True 

if is_palendrome: print('Да, это палиндром!')



