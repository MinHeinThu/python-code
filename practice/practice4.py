class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying")

class SportPerson:
    def __init__(self, sport):
        self.sport = sport

    def play_sport(self):
        print(f"Play {self.sport}")

class StudentAthlete(Student, SportPerson):
    def __init__(self,name, sport):
        Student.__init__(self,name)
        SportPerson.__init__(self, sport)

    def show_details(self):
        super().study()
        super().play_sport()

student1 = StudentAthlete("Jack", "football")
student1.show_details()