import random

class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

def generate_random_student():
    full_name = f"{random.choice(['Иван', 'Анатолий', 'Александр', 'Павел', 'Артур', 'Олег', 'Артем', 'Алексей', 'Даниил'])} {random.choice(['Савин', 'Ланьков', 'Иванов', 'Петров', 'Сергеев', 'Топорков', 'Солдатов', 'Колокольников', 'Дробышев', 'Потапов'])}"
    group_number = f"Группа {random.randint(1, 2)}"
    grades = [random.randint(3, 5) for _ in range(5)]

    return Student(full_name, group_number, grades)

students = [generate_random_student() for _ in range(10)]

sorted_students = sorted(students, key=lambda student: student.average_grade(), reverse=True)

print("Студенты, отсортированные по среднему баллу:")
for student in sorted_students:
    print(f"{student.full_name}, Группа: {student.group_number}, Средний балл: {student.average_grade()}")
