error_pattern = 'Ошибка: менее трёх символов в строке {}.'
symbols_count = 0

with open('test/people.txt', 'r', encoding='utf-8') as people_file, open('errors.log', 'a', encoding='utf-8') as log_file:
    for line_i, line in enumerate(people_file):
        try:
            length = len(line) - line.count('\n')
            symbols_count += length
            if length < 3:
                raise ValueError(error_pattern.format(line_i + 1))
        except ValueError:
            print(error_pattern.format(line_i + 1))
            log_file.write(error_pattern.format(line_i + 1) + '\n')
  
print(f'Общее количество символов: {symbols_count}.')