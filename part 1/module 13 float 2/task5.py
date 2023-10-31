start_amplitude = float(input('Введите начальную амплитуду: '))
end_amplitude = float(input('Введите конечную амплитуду: '))

if start_amplitude <= 0:
    print("Амплитуда должна быть положительным числом.")
elif end_amplitude < 0: 
    print("Амплитуда остановки должна быть неотрицательным числом.")
else: 
    count = 0
    while(start_amplitude > end_amplitude): 
        start_amplitude -= start_amplitude * (8.4 / 100)
        count += 1
        
    print(f'Маятник считается остановившимся через {count} колебаний')