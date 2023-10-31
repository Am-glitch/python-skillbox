def countletters():
    text = input('Введите текст: ')
    digit = input('Какую цифру ищем? ')
    letter = input('Какую букву ищем? ')
    
    digit_count = text.count(letter)
    letter_count = text.lower().count(digit)

    print(f"\nКоличество цифр {digit}: {digit_count}")
    print(f"Количество букв {letter}: {letter_count}")

countletters()