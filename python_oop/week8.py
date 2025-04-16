class Department:
    def __init__(self, name):
        self.name = name
class Teacher:
    def __init__(self, name, department):
        self.name = name
        self.department = department


dept = Department("CS")

t1 = Teacher("Ali", dept)
t2 = Teacher("Sarr", dept)

print(t1.department.name)


