class Department:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department 

    def show_details(self):
        print(f"Teacher Name: {self.name}, Department: {self.department.name}")


dept = Department("CS")
teacher1 = Teacher("Ms.Juli", dept)
print(teacher1.name)
print(teacher1.department.name) # Aggregation has realationship but weak
teacher1.show_details()


# Composition has a relationship but strong

class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()
        print("Car is moving")

my_car = Car()
my_car.drive()
