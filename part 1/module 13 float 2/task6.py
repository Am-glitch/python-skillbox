def danger_level(x):
    return x**3 - 3*x**2 - 12*x + 10

def find_safe_depth(max_danger):
    epsilon = 1e-6  
    x = 0.0

    while abs(danger_level(x)) > max_danger and x < 4.0:
        x += epsilon

    return x
    

def main():
    while True:
        max_danger = float(input("Введите максимально допустимый уровень опасности: "))
        if max_danger < 0:
            print("Введите корректное число.")
        else: 
            break

    safe_depth = find_safe_depth(max_danger)

    if safe_depth is not None:
        print(f"Приблизительная глубина безопасной кладки: {safe_depth:.7f} м")

main()
