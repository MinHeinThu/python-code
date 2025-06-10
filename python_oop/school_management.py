"""
Name: Min Hein Thu
ID: 67111391
Date: 19/ April / 2025
"""

class Person:
    def __init__(self, name):
        self.name = name

    def show_info(self): # Show info method
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject.subject_name}")

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def study(self):
        # print(f"Name: {self.name.name}")
        print(f"{self.name} is studying")

class Subject: # Aggregation subject class and it will to pass subject object ot Teacher class
    def __init__(self, subject_name):
        self.subject_name = subject_name

class Classroom: # Composition 
    def __init__(self):
        
        """
        This one is first method I use and I assing the value inside the class
        """
        # self.student = Student("Jay")
        # self.teacher = Teacher("Ms. Tina", subject)

        """
        This one is second method and I feel like traditional way we usually code
        """
        self.student = student
        self.teacher = teacher

    def start_class(self):
        print("Class is staring...\n")
        """
        we can use parent class method that is show_info() cause teacher and student is child class
        """
        self.teacher.show_info()
        self.teacher.teach()
        self.student.show_info()
        self.student.study()
        print("\nClass has ended.")

""" 
 If I wnat to use first method I need to remove the the student and teacher objects 
"""
subject = Subject("Mathematics") # subject object need to assign before teacher when I use second method
student = Student("Jay")
teacher = Teacher("Ms. Tina", subject)


classroom = Classroom()
classroom.start_class()


"""
Even if I understand the concept of composition and aggregation a little bit comfuse to implement idea to code
"""
