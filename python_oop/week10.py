class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def save(self):
        try: 
            with open("student.txt", "a") as file:
                file.write(f"{self.name},{self.grade}\n")
        except Exception as e:
            print("Failed to save student:", e)
    
    @staticmethod
    def display_all():
        try:
            with open("student.txt", "r") as file:
                # print("All Students:")
                for line in file:
                    name, grade = line.strip().split(",")      
                    print(f"Name: {name}, Grede: {grade}")
        except FileNotFoundError:
            print("No student records found.")


student1 = Student("Hello", "10")
student1.save()
Student.display_all()