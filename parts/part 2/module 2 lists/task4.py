films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
liked_films = []

amount = int(input('Сколько фильмов хотите добавить? '))


for film in range(amount):
    film_name = input('Введите название фильма: ')
    if film_name not in films: 
        print(f'Ошибка: фильма {film_name} у нас нет :(')
    else: 
        liked_films.append(film_name)

print('Ваш список любимых фильмов:', ', '.join(liked_films))


    