message = input('Введите зашифрованное сообщение: ')

decripted_message = []
# counter = 1
# for symbol in message:
#     if counter % 2 != 0: 
#         decripted_message = symbol + decripted_message
#     else: 
#         decripted_message += symbol
#     counter += 1

left_pointer = 0
right_pointer = 0
for i in range(len(message)):
    if i % 2 != 0: 
        decripted_message.insert(left_pointer, message[i])
        right_pointer += 1
        
    else: 
        decripted_message.insert(len(decripted_message) - right_pointer, message[i])
        left_pointer += 1
        
print('расшифрованное слово:', ''.join(decripted_message))
