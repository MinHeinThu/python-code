class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    def set_salary(self, basic, bonus = 0):
        self.salary = basic + bonus

        print(f'Updated salary for {self.name}: {self.salary}')

# Creating an employee

emp = Employee('Alic', 50000)

