class Person:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

    def study(self):
        print(f"{self.name} is studying")

stu1 = Student('Ali')
stu1.show_info()
stu1.study()