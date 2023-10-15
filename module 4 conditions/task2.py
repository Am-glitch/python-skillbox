first_grade = int(input('Введите количество баллов по русскому языку: '))
second_grade = int(input('Введите количество баллов по математике: '))
third_grade = int(input('Введите количество баллов по информатике: '))

if first_grade + second_grade + third_grade >= 270: 
    print('Поздравляю, ты поступил на бюджет!')
else: print('К сожалению, ты не прошёл на бюджет.')