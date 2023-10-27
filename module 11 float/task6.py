x_knight = float(input("Введите координату x для коня: "))
y_knight = float(input("Введите координату y для коня: "))

x_point = float(input("Введите координату x для точки: "))
y_point = float(input("Введите координату y для точки: "))

diff_x = abs(x_knight - x_point)
diff_y = abs(y_knight - y_point)

can_move = diff_x * diff_y == 2

print(f"Конь в клетке ({x_knight}, {y_knight}). Точка в клетке ({x_point}, {y_point}).")
print("Да, конь может ходить в эту точку." if can_move else "Нет, конь не может ходить в эту точку.")
