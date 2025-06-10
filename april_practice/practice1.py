class Department:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department

dept = Department("CS")
teacher1 = Teacher("Ali", dept)
teacher1 = Teacher("Jli", dept)

print(teacher1.department.name)