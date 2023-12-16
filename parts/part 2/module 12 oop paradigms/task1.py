class Property:
    def __init__(self, worth):
        self.worth = worth

    def calculate_tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500


def main():
    money = float(input("Введите количество ваших денег: "))
    property_worth = float(input("Введите стоимость вашего имущества: "))

    apartment = Apartment(property_worth)
    car = Car(property_worth)
    country_house = CountryHouse(property_worth)

    apartment_tax = apartment.calculate_tax()
    car_tax = car.calculate_tax()
    country_house_tax = country_house.calculate_tax()

    total_tax = apartment_tax + car_tax + country_house_tax

    print(f"Налог на квартиру: {apartment_tax:.2f}")
    print(f"Налог на машину: {car_tax:.2f}")
    print(f"Налог на дачу: {country_house_tax:.2f}")

    if money < total_tax:
        print(f"Вам не хватает {total_tax - money:.2f} денег для уплаты налога.")
    else:
        print("У вас достаточно денег для уплаты налога.")


if __name__ == "__main__":
    main()
