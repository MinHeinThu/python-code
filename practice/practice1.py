# this practice is crror handling in python
"""

There are two main types of errors in pyhont:
1. Syntax Error : This happen when you break the rule of the python code

2. Runtime Error (Ecception)
A runtime error happens when your code runs correctly at first, but something goes wrong while it's running

' A type of error that occurs during program execution'

"""

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result: ","%.2f"  % result)
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("Program ended.")

""" Raise keyword is use when we want to coutomize the error """

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age should not be negative")
else:
    print("Your age is:", age)


# Error handling  Inside a class
class Student:
    def __init__(self, name, marks):
        if marks < 0:
            raise ValueError("Marks is no negative")
        else:
            self.marks = marks
        self.marks = marks
try:
    s1 = Student("Ali", -20)
except ValueError as e:
    print("Error:", e)

class InvalidMarksError(Exception):
    pass

class Score:
    def __init__(self, score):
        pass