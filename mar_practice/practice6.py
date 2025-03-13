from abc import ABC, abstractmethod
class Employee(ABC):
    def display_employee_details(self, name):
        print(f"Enployee: {name}")

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def show_benefits(self):
        pass

class FullTimeEmployee(Employee):

    def calculate_salary(self):
        print("Montly salary: 5000$")

    def show_benefits(self):
        print("Benefits: Health Insurance Provided")

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        print("Monthly salary: 4000$")

    def show_benefits(self):
        print("Benefits: No additional benefits")

full = FullTimeEmployee()
full.display_employee_details("ali")
full.calculate_salary()
full.show_benefits()