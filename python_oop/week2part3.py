class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f'{self.name} is Studying')

class SportPerson:
    def __init__(self,sport):
        self.sport = sport

    def play_sport(self):
        print(f'{self.sport} is favourite sport')

class StudentAthlete(Student, SportPerson):
    def __init__(self, name, sport):
        super(Student, SportPerson).__init__()

    
    def show_detail(self):
        super().study()
        super().play_sport()
        

p1 = StudentAthlete("John", "Football")
p1.show_detail()