class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f'Name: {self.name}, Salary: {self.salary}')
    

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def show(self):
        super().show()
        print(f'Team Size: {self.team_size}')
    
emp = Employee('John', 50000)
print('Employee Details')
emp.show()

print('\nManager Details')

mgr = Manager('Alice', 80000, 10)
mgr.show()

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def show_details(self):
        print(f'Brand: {self.brand}, Speed: {self.speed} km/h')


class Car(Vehicle):
    def __init__(self, brand, speed, price):
        super.__init__(brand, speed)
        self.price = price
    def show_details(self):
        super().show_details()
        print(f'Price: {self.type}')

class Bicycle(Vehicle):
    def __init__(self, brand, speed, passenger):
        super.__init__(brand, speed)
        pass