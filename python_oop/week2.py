# Class of mobile phone
class MobilePhone:
    # Instructor
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Return str
    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.brand}, Price: {self.price}'
    
# Two objects
phone1 = MobilePhone("apple","16 pro max", 50000)
phone2 = MobilePhone('Samsung', "22pro", 45000)

# Show details of Mobile Phone
print(phone1)
print(phone2)


class UniversityStudents:
    def __init__(self, name, id, major, gpa):
        self.name = name
        self.id = id
        self.major = major
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying at {self.major} majors")

    def attend_class(self):
        print(f"{self.name} with id: {self.id} attend the class {self.major}")

    def give_exam(self):
        print(f"{self.name} is got GPA {self.gpa}")


student1 = UniversityStudents("Joe", 1, 'Ict', 3.0)
student2 = UniversityStudents("Alic", 2, 'Ict', 3.2)


student1.study()
student1.attend_class()
student1.give_exam()

student2.study()
student2.attend_class()
student2.attend_class()

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_details(self):
        print(f'Brand:{self.brand}, Speed:{self.speed} km/h')

class Car(Vehicle):
    def __init__(self,brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def show_details(self):
        super().show_details()
        print(f'Doors: {self.doors}')

car1 = Car('Toyota', 180, 4)
car1.show_details()

# Single inheritance 
class Animal:
    def speak(self):
        print('Animals make sound')

class Dog(Animal):
    def bark(self):
        print('Dog barks')

# 
dog = Dog()
dog.speak()
dog.bark()

# Multilevel inheritance
class Animal:
    def breath(self):
        print("Breathing...")

class Mammal(Animal):
    def has_fur(self):
        print("has fur")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()

dog.breath()
dog.has_fur()
dog.bark()

# Multiple inheritance
class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def rotate(self):
        print("Wheels rotaing")

class Car(Engine, Wheels):
    def drive(self):
        print('Car is driving')

my_car = Car()
my_car.start()
my_car.rotate()
my_car.drive()