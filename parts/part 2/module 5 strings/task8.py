def can_shift(str1, str2):
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        shifted_str = str2[i:] + str2[:i]
        if shifted_str == str1:
            return i

    return False

first_string = input("Первая строка: ")
second_string = input("Вторая строка: ")

result = can_shift(first_string, second_string)

if result:
    print(f"Первая строка получается из второй со сдвигом {result}.")
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
