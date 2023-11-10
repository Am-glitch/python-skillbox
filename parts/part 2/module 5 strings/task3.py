file_name = input('Название файла: ')

if file_name.startswith(tuple(['@', '№', '$', '%', '^', '&', '*'])): 
    print('Ошибка: название начинается недопустимым символом.')
elif not file_name.endswith(tuple(['.txt', '.docx'])):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
