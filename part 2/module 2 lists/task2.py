names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

every_second_names = [names[index] for index in range(len(names)) if index % 2 == 0]
print(every_second_names)