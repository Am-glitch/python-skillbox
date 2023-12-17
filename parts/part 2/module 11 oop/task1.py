import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, enemy):
        damage = 20
        enemy.health -= damage
        print(f"{self.name} атаковал {enemy.name}. {enemy.name} осталось здоровья: {enemy.health}")

warrior1 = Warrior("Воин 1")
warrior2 = Warrior("Воин 2")

while warrior1.health > 0 and warrior2.health > 0:
    attacker = random.choice([warrior1, warrior2])
    enemy = warrior2 if attacker == warrior1 else warrior1

    attacker.attack(enemy)

print(f"{warrior1.name if warrior1.health > 0 else warrior2.name} одержал победу!")
