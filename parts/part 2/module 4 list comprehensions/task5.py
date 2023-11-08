string = input('Введите строку: ')

first_index = string.index('h')
second_index = string.rindex('h')

print('Развёрнутая последовательность между первым и последним h:', string[second_index - 1:first_index:-1])