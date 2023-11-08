def crypt(message):
    result = ""
    for char in message:
        if char.isalpha():  
            start = ord('А') if char.isupper() else ord('а')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

message = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

print('Зашифрованное сообщение:', crypt(message))  #ахс тлхср.