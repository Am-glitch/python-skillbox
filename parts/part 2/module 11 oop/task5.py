import random

print('Задача 7. Совместное проживание')


class House:
    def __init__(self):
        self.food_amount = 50
        self.money = 0

    def __str__(self):
        return f'Деньги: {self.money}. Еда: {self.food_amount}'


class Human:
    def __init__(self, name: str, house: House):
        self.name = name
        self.house = house
        self.satiety = 50

    def eat(self, amount: int):
        amount = min(amount, self.house.food_amount)
        if amount == 0:
            return False
        self.satiety += amount
        self.house.food_amount -= amount
        return True

    def work(self, amount: int):
        amount = min(amount, self.satiety)
        if amount == 0:
            return False
        self.house.money += amount
        self.satiety -= amount
        return True

    def play(self, amount: int):
        amount = min(amount, self.satiety)
        self.satiety -= amount

    def buy_food(self, amount: int):
        amount = min(amount, self.house.money)
        if amount == 0:
            return False
        self.house.food_amount += amount
        self.house.money -= amount
        return True

    def is_dead(self):
        return self.satiety == 0

    def do_action(self, amount: int):
        if self.is_dead():
            raise SyntaxError
        if self.satiety < 20 and self.eat(amount):
            return
        if self.house.food_amount < 10 and self.buy_food(amount):
            return
        if self.house.money < 50 and self.work(amount):
            return
        if amount == 1 and self.work(amount):
            return
        if amount == 2 and self.eat(amount):
            return
        self.play(amount)

    def __str__(self):
        return f'{self.name}. Сытость: {self.satiety}'


house = House()
human1 = Human('Антон', house)
human2 = Human('Евгения', house)

for day in range(1, 366):
    print(f'\nДень {day}:')
    print(f'Состояние дома: {house}')
    print('Состояние жителей:')
    print(human1)
    print(human2)
    if human1.is_dead() or human2.is_dead():
        if human1.is_dead():
            print(f'{human1.name} умер(-ла) (( ')
        if human2.is_dead():
            print(f'{human2.name} умер(-ла). ((')
        break
    human1.do_action(random.randint(1, 6))
    human2.do_action(random.randint(1, 6))
else:
    print('\nЖители успешно прожили год!')