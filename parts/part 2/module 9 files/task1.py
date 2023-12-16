import re

def get_numbers(data: str):
    return [int(number) for number in re.split('[^0-9]+', data) if number.isnumeric()]

numbers_file = open('numbers.txt', 'r')
numbers_data = numbers_file.read()
numbers_file.close()

numbers = get_numbers(numbers_data)

result = sum(numbers)
answer_file = open('answer.txt', 'w')
answer_file.write(str(result))
answer_file.close()

print('\nСодержимое файла numbers.txt')
print(numbers_data)

print('\nЧисла из файла')
print(numbers)

print('\nСодержимое файла answer.txt')
print(result)