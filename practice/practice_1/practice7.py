# class Student:
#     school_name = "Green School"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def get_school(cls):
#         print("School name is: ",cls.school_name)

# Student.get_school()

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def save(self):
        try:
            with open("student1.txt", "a") as file:
                file.write(f"{self.name},{self.grade}\n")
        except Exception as e:
            print("Failed to save student:", e)

    @staticmethod
    def display_all():
        try:
            with open("student1.txt", "r") as file:
                # print("All students: ")
                for line in file:
                    name, grade = line.strip().split(",")
                    print(f"Name: {name}, Grade: {grade}")
        except FileNotFoundError:
            print("No students records found.")

s1 = Student("Jack", "12")
s1.save()
Student.display_all()
