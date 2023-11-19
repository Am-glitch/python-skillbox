def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def crypto(enum):
    return [value for index, value in enumerate(enum) if is_prime(index)]
    

print(crypto('О Дивный Новый мир!'))


