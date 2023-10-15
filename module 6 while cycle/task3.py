number = int(input('Введите число: '))

divider = 10
count = 1
while(True):
    if ((number % divider == number) or (number == 0)):
        print(count)
        break 
    divider *= 10
    count += 1
    
    

