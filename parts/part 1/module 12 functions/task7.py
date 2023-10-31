import random 


def rock_paper_scissors():
    print("Игра 'Камень, ножницы, бумага'")
    choices = ['Камень', 'Ножницы', 'Бумага']

    
    while(True):
        player_choice = input("Выберите (Камень, Ножницы, Бумага): ").capitalize()
        if(player_choice in choices):
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
        

    computer_choice = random.choice(choices)
    print(f"Компьютер выбрал: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 'Камень' and computer_choice == 'Ножницы') or \
         (player_choice == 'Ножницы' and computer_choice == 'Бумага') or \
         (player_choice == 'Бумага' and computer_choice == 'Камень'):
        print("Вы победили!")
    else:
        print("Вы проиграли.")

def guess_the_number():
    print("Игра 'Угадай число'")
    number_to_guess = random.randint(1, 50)

    print("Угадайте число от 1 до 50.")

    while(True):
        guess = int(input("Введите ваш вариант: "))
        if guess == number_to_guess:
            print("Поздравляем, вы угадали!")
            return
        elif guess < number_to_guess:
            print("Число больше. Попробуйте еще раз.")
        else:
            print("Число меньше. Попробуйте еще раз.")


def mainMenu():
    print('Выберите игру: ')
    choice = input('1-Камень, ножницы, бумага\n2-Угадай число\n')

    if choice == '1':
        rock_paper_scissors()
    elif choice == '2':
        guess_the_number()
    else:
        print('Попробуйте еще раз')

mainMenu()