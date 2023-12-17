class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"

    @classmethod
    def from_string(cls, date_str: str):
        day, month, year = map(int, date_str.split('-'))
        if cls.is_date_valid(day, month, year):
            return cls(day, month, year)
        else:
            raise ValueError("Некорректная дата")

    @staticmethod
    def is_date_valid(day: int, month: int, year: int) -> bool:
        if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
            return True
        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid(10, 12, 2077))
print(Date.is_date_valid(40, 12, 2077))
