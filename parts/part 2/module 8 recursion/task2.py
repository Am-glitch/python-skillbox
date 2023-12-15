def recursive_find(dictionary, target_key, max_depth=None, current_depth=1):
    if target_key in dictionary.keys():
        print(f"Значение ключа '{target_key}': {dictionary.get(target_key)}")
        return
    
    if max_depth is not None and current_depth >= max_depth:
        print('Значение ключа: None')
        return

    for _, value in dictionary.items():
        recursive_find(value, target_key, max_depth, current_depth + 1)

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

target_key = input("Введите искомый ключ: ")

max_depth_input = input("Хотите ввести максимальную глубину? Y/N: ").lower()
max_depth = None

if max_depth_input == 'y':
    max_depth = int(input("Введите максимальную глубину: "))

recursive_find(site, target_key, max_depth)