class Car:
    def __init__(self, brand, speed):
        self._brand = brand
        self._speed = speed

class SportCar(Car):
    def show_details(self):
        print(f'Car brand: {self._brand} and the max speed is {self._speed}')


car1 = SportCar('BMW', 250)
car1.show_details()

car1._brand = 'Toyota'
print(car1._brand)
car1.show_details()


