import re

def check_phone_numbers(phone_numbers):
    for number in phone_numbers:
        if re.match(r'^[89]\d{9}$', number):
            print(f'{number}: всё в порядке')
        else:
            print(f'{number}: не подходит')


if __name__ == '__main__':
    phone_numbers = ['9999999999', '999999-999', '99999x9999']
    check_phone_numbers(phone_numbers)


