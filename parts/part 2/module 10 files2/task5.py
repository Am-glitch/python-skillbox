import math

def calculate_square_root(number):
    try:
        if number < 0:
            raise ValueError("Отрицательные числа не поддерживаются.")
        result = math.sqrt(number)
        return result
    except ValueError as ve:
        return f"Ошибка: {ve}"
    except Exception as e:
        return f"Произошла ошибка: {e}"


try:
    input_number = float(input("Введите число: "))
    result = calculate_square_root(input_number)
    print(f"Квадратный корень: {result}")
except ValueError as ve:
    print(f"Ошибка ввода: {ve}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
