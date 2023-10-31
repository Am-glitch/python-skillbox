N = 0
attempts = 0

lower_bound = 1
upper_bound = 100

while True:
    N = (lower_bound + upper_bound) // 2
    print(f"Ваше число равно, меньше или больше {N}?")
    print("Введите 1, если равно, 2, если больше, 3, если меньше.")
        
    user_input = int(input())

    if user_input == 1:
        print(f"Компьютер угадал ваше число {N} за {attempts + 1} попыток.")
        break
    elif user_input == 2:
        lower_bound = N + 1
    elif user_input == 3:
        upper_bound = N - 1

    attempts += 1

    if attempts >= 7:
        print("Компьютер не смог угадать число за 7 попыток.")
        break
        