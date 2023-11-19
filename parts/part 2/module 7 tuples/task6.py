contacts = dict()

while True:
    operation = input('Введите номер действия: \n1)Добавить контакт. \n2)Найти человека.\n')
    if operation == '1':
        contact_name_string = input('Введите имя и фамилию нового контакта (через пробел): ')
        contact_name = tuple([word for word in contact_name_string.split()])
        if contact_name in contacts:
            print('Такой человек уже есть в контактах.')
            print('Текущий словарь контактов:', contacts)
            continue
        phone_number = input('Введите номер телефона: ')
        contacts[contact_name] = phone_number
        print('Текущий словарь контактов:', contacts)
    elif (operation == '2'):
        surname = input('Введите фамилию для поиска: ')
        for contact_name in contacts:
            if (contact_name[1] == surname):
                print(contact_name[0], contact_name[1], contacts[contact_name])

        
    