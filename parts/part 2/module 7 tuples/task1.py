students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology', 'swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}

#Написать функцию, которая принимает в качестве аргумента словарь и 
# возвращает два значения: полный список интересов всех студентов 
# и общую длину всех фамилий студентов.
def examine_dict(students_dict):
    interests_total = set()
    surnames_length = 0
    for _, student_info in students_dict.items():
        interests_total.update(student_info['interests'])
        surnames_length += len(student_info['surname'])

    return list(interests_total), surnames_length

#Вывести на экран список пар «ID студента — возраст»
for student_id, student_info in students.items():
    print(f'{student_id} - {student_info["age"]}')


print(examine_dict(students))