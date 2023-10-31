numbers = [int(x) for x in input('Введите последовательность чисел: ').split()] 

for order in range(len(numbers)-1, -1, -1): 
    if numbers[order] % 2 == 0: 
        print(f'{numbers[order]}', end=' ') 