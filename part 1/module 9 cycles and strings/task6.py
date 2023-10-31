states = [state for state in input('Какие стойла свободны?: ').split()]

count = 0
for index in range(len(states)):
    if states[index] == 'b':
        count += (index + 1) * 2

print(f'произведено молока за день: {count}')