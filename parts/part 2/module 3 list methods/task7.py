def last_person_standing(num_people, k):
    people = list(range(1, num_people + 1))
    
    current_index = 0
    
    while len(people) > 1:
        current_index = (current_index + k - 1) % len(people)
        print('Текущий круг людей:', people)
        removed_person = people.pop(current_index)
        print(f"Выбывает человек под номером {removed_person}")
        input()
    return people[0]

num_people = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))

result = last_person_standing(num_people, k)
print(f"\nОстался человек под номером {result}")
