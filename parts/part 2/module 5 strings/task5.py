while(True):
    password = input('Придумайте пароль: ')
    if (len(password) >= 8 and any(char.isupper() for char in password) and sum(char.isdigit() for char in password)):
        print('Это надежный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')