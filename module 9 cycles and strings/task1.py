enterCount = 0

for pirate in range(10):
    word = input('Крикни слово: ')
    if word == 'Карамба' or word == 'карамба': 
        enterCount += 1

print(f'На борт попало пиратов: {enterCount}')
