file_size = int(input('Размер файла для скачивания: '))
connection_speed = int(input('Скорость соединения: '))

downloaded = 0
seconds = 0

while downloaded < file_size:
    seconds += 1
    downloaded += connection_speed

    if downloaded > file_size:
        downloaded = file_size

    percentage = (downloaded / file_size) * 100

    print(f"Прошло {seconds} сек. Скачано {downloaded} из {file_size} Мб ({percentage:.2f}%)")

print(f"\nСкачивание завершено за {seconds} сек.")