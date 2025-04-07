# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def show(self):
#         print(f"Name: {self.name}: Salary: {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size

#     def show(self):
#         super().show()
#         print(f"Team size: {self.team_size}")

# emp = Manager("jack", 4000, 22)
# emp.show()

class Student:
    def __init__(self, name):
        self.name = name
    
    def study(self):
        print(f"{self.name} is study")

class SportPerson:
    def __init__(self, sport):
        self.sport = sport
    
    def play_sport(self):
        print(f"{self.sport} is good sport")

class StudentAthlete(Student, SportPerson):
    def __init__(self, name, sport):
        Student.__init__(self,name)
        SportPerson.__init__(self, sport)

    def show_details(self):
        super().study()
        super().play_sport()


student1 = StudentAthlete("Loli","football")
student1.show_details()