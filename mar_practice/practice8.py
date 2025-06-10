class Student:
    def __init__(self, grade):
        self.__grade = grade
    
    def set_grade(self, new_grade):
        valid_grades = ["A", "B", "C", "D", "F"]
        if new_grade in valid_grades:
            self.__grade = new_grade
        else:
            print("Invalid grade")  

    def get_grade(self):
       return self.__grade
    
student1 = Student("B")
print(student1.get_grade())
student1.set_grade("C")
print(student1.get_grade())


    

