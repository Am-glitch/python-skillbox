#not yet done
import random

class KarmaError(RuntimeError):
    def __str__(self):
        return 'Error '


class KillError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], str(type(self).__name__)))


class DrunkError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], str(type(self).__name__)))


class CarCrushError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], str(type(self).__name__)))


class GluttonyError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], str(type(self).__name__)))


class DepressionError(KarmaError):
    def __str__(self):
        return ': '.join((super().__str__()[:-1], str(type(self).__name__)))


KARMA_ERRORS = [KillError(), DrunkError(), CarCrushError(), GluttonyError(), DepressionError()]


def one_day():
    if random.randint(1, 10) == 1:
        raise random.choice(KARMA_ERRORS)
    return random.randint(1, 7)


REQURED_KARMA = 500

karma_collected = 0
day = 1

with open('karma.log', 'w', encoding='utf-8') as log:
    while karma_collected < REQURED_KARMA:
        try:
            karma_collected += one_day()
        except KarmaError as e:
            log.write(f'День {day}: {e}\n')
        day += 1

print(f'Карма в количестве {REQURED_KARMA} накоплена за {day} дней.')