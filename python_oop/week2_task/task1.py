# Name: Min Hein Thu
# ID: 67111391
# Task 1: University System (Multiple Inheritance)

# Multiple inheritance
class Student:
    # Constructor
    def __init__(self, name):
        self.name = name
    
    # Method
    def study(self):
        return f'{self.name} studies'
    
class SportPerson:
    # Constructor
    def __init__(self, sport):
        self.sport = sport
    
    # Method
    def play_sport(self):
        return f'{self.sport} is good sport'
    
class StudentAthlete(Student,SportPerson):
    # Constructor 
    def __init__(self, name, sport):
        Student.__init__(self, name)
        SportPerson.__init__(self, sport)
    
    # Method
    def show_details(self):
        return f'Name: {self.name}\nFavourite Sport: {self.sport}'

# Object
student1 = StudentAthlete("Loli","football")
print(student1.show_details())
# print(student1.study())
# print(student1.play_sport())
