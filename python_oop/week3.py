def add_numbers(*args):
    print(args)
    return args

print(add_numbers(2,3))
print(add_numbers(2,3,4,5))
print(add_numbers(10))
add = add_numbers(10)
print(type(add))


class Employee:
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary

    
    def work(self):
        print(f'{self.name} is working')


class Manager(Employee):
    # def __init__(self, name, salary):
    #     super().__init__(name, salary)

    
    def work(self):
        print(f'{self.name} is managing the team')

class Developer(Employee):
    # def __init__(self, name, salary):
    #     super().__init__(name, salary)

    def work(self):
        print(f'{self.name} is writhing code')

class Intern(Employee):
    # def __init__(self, name, salary):
    #     super().__init__(name, salary)

    def work(self):
        print(f'{self.name} is learning new skills')


# d = Developer("Jack", 10)
# d.work()

employees = [Manager('Ali', 8000), Developer('Dara', 4000), Intern('Na', 200)]

for emp in employees:
    emp.work()