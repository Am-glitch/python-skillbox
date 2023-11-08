violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]
new_playlist = []
total_time = 0

amount = int(input('Сколько песен выбрать? '))

for i_song in range(amount):
    song = input(f'Название {i_song + 1}-й песни: ')
    new_playlist.append(song)

for i_song in range(len(violator_songs)):
    if violator_songs[i_song][0] in new_playlist:
        total_time += violator_songs[i_song][1]

print(f'Общее время звучания песен — {total_time:.2f} минуты')
