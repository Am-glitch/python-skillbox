def is_palindrome_possible(input_string):
    char_count = {}

    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    if len(input_string) % 2 == 0 and odd_count == 0:
        return True
    elif len(input_string) % 2 != 0 and odd_count == 1:
        return True
    else:
        return False

word = input("Введите строку: ")

if is_palindrome_possible(word):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")


