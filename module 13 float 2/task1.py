def convert_to_float_format(x):
    a, b = "{:.9e}".format(x).split('e')
    a = float(a)
    b = int(b)
    precision = len(str(a).split('.')[1]) if '.' in str(a) else 0

    print(f"Формат плавающей точки: x = {a:.{precision}f} * 10 ** {b}")


while True:
    x = float(input("Введите число: "))
    if x > 0:
        break
    else:
        print("Число должно быть больше нуля.")

convert_to_float_format(x)




