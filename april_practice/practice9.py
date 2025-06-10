class Car:
    def __init__(self, brand, speed):
        self._brand = brand
        self._speed = speed

    
class SportCar(Car):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def show_details(self):
        print(f"Brand: {self._brand}, Speed: {self._speed}")

car1 = SportCar("Toyota", 120)

car1.show_details()
car1.show_details()
car1.show_details()



class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def _withdraw(self, amount):
        self._balance -= amount
        print(f"Withdrawn: {amount}")
        print(f"New Balance: {self._balance}")

class SavingAccount(BankAccount):
    def withdra_amounnt(self, amount):
        print("Processing wihtdrawal...")
        self._withdraw(amount)
        print("Transaction Complete.")

savings = SavingAccount(1000)

savings.withdra_amounnt(339)