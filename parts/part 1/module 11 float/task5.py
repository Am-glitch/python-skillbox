import math

earth_volume =  1.08321 * 10 ** 12 

radius = int(input('Введите радиус случайной планеты: '))

object_volume = (4 / 3) * math.pi * radius ** 3

ratio = earth_volume / object_volume

print(f"Объем планеты Земля {'больше' if ratio > 1 else 'меньше'} в {abs(round(ratio, 3))} раз")