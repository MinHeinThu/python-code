from abc import ABC, abstractmethod

class School:
    def __init__(self, name):
        self.name = name
    def get_info(self):
        return self.name
    
class Person(ABC):
    def __init__(self, name, email, contact):
        self.name = name
        self._email= email
        self.__contact = contact
    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact):
        if len(contact) == 11:
            self.__contact = contact
        else:
            raise ValueError("Contact must be 11 digits")
    @abstractmethod
    def show_role(self):
        pass
class Student(Person):
    total_student = 0
    def __init__(self, name, email, contact, roll_no, grades):
        super().__init__(name, email, contact)
        self.roll_no = roll_no
        self.grades = grades
        Student.total_student += 1

    def add_grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)
        return
        return
    
    def average_grade(self):
        return sum(self.grades)/len(self.grades)
    
    def show_role(self):
        print("I am a Student")

    def __str__(self):
        return f"Student Name: {self.name}, Roll No: {self.roll_no}, Average Grade: {self.average_grade()}"
    
    @classmethod
    def get_total_student(cls):
        return cls.total_student
    
class Teacher(Person):
    def __init__(self, name, email, contact, subject, salary):
        super().__init__(name, email, contact)
        self.subject = subject
        self.salary = salary

    def show_role(self):
        print("I am a Teacher")
    
    def __str__(self):
       return f"Name: {self.name}, Subject: {self.subject}"

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher  # Aggregation: Course has a Teacher
        self.students = []      # Composition: Course manages its students list

    def enroll(self, student):
        self.students.append(student)
        return
    
    def course_info(self):
        return f"Course Title: {self.title}, Teacher Name: {self.teacher.name}, Number of enrolled students: {len(self.students)}"

class AdminPortal:
    @staticmethod
    def save_student_data(student):
        with open("students.txt", "a") as file:
            file.write(student)
    
    @staticmethod
    def save_teacher_data(teacher):
        with open("teachers.txt", "a") as file:
            file.write(teacher)


# Test Area 
person1 = ("Ali", "Something@email", "01234567890")
person2 = ("Jack", "nothing@email.com", "09876543210")
person3 = ("Ms.Sora", "happy@email.com", "12345678901")

# 1
school = School("Krirk Uinversity")
print(school.get_info()) # works

# 2
student1 = Student(person1[0], person1[1], person1[2], "A", [1, 2, 3, 4]) # name, email, contact, roll, grades
student2 = Student(person2[0], person2[1], person2[2], "B", [1, 3, 2, 4])
teacher = Teacher(person3[0], person3[1], person3[2], "OOP", 2000) # name, email, contact, subject, salary
# 3
student1.contact = "98765432112" # work 
print(student1.contact) # work

# 4  
course = Course("OOP", teacher)
course = Course("OOP", teacher)

# 5
course.enroll(student1)
course.enroll(student2)

# 6
student2.show_role()
student1.show_role()
teacher.show_role()

# 8
print(course.course_info())

#7
print(student1)

# 9
AdminPortal.save_student_data(str(student1))
AdminPortal.save_teacher_data(str(teacher))

# 10
print(Student.get_total_student())
