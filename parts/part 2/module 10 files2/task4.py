from typing import TextIO


MESSAGE_TEMPLATE = "'{}': '{}'\n"

def get_user_action():
    print('\nВыберите одно из действий:')
    print('\t 1. Посмотреть текущий текст чата.')
    print('\t 2. Отправить сообщение.')
    print('\t 3. Выход.')
    return input('Введите номер действия (число 1, 2 или 3): ')


def display_chat(chat_file: TextIO):
    print('\nПредыдущие сообщения чата:\n')
    chat_file.seek(0)
    print(chat_file.read())


def send_message(username: str, chat_file: TextIO):
    message = input('Введите сообщение: ')
    chat_file.write(MESSAGE_TEMPLATE.format(username, message))


user_name = input('Введите ваше имя: ')

with open('test/chat.txt', 'a+', encoding='utf-8') as chat_file:
    while True:
        try:
            action = get_user_action()
            if action == '1':
                display_chat(chat_file)
            elif action == '2':
                send_message(user_name, chat_file)
            elif action == '3':
                break
            else:
                print('Нет такой команды. Попробуйте ещё раз.')
        except BlockingIOError:
            print('В текущий момент с чатом работает другой пользователь.')
            print('Подождите немного и повторите попытку.')
