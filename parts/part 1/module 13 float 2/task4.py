def count_number(number):
    num_count = 0
    temp = number

    while temp > 0:
        num_count += 1
        temp = temp // 10

    return num_count

def change_number(number):
    num_count = count_number(number)
    last_digit = number % 10
    first_digit = number // 10 ** (num_count - 1)
    between_digits = number % 10 ** (num_count - 1) // 10
    number = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit
    return number

def main(): 
    first_n = int(input("Введите первое число: "))
    second_n = int(input("Введите второе число: "))
    
    if count_number(first_n) >= 3:
       print('Изменённое первое число:', change_number(first_n))
    else: 
       print("В первом числе меньше трёх цифр.")

    if count_number(second_n) >= 4:
       print('Изменённое второе число:', change_number(second_n))
       print('\nСумма чисел:', first_n + second_n)
    else: 
       print("В первом числе меньше четырёх цифр.")
    

main()
    
    

