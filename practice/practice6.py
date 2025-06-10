class InvalidMarksError(Exception):
    pass

class Student:
    def __init__(self, name, marks):
        self.name = name
        if marks < 0:
            raise InvalidMarksError("Marks should be positive")
        else:
            self.marks = marks

    
try:
    s2 = Student("Ali", 3)
except InvalidMarksError as e:
    print("Coustom error: ", e)