"""
r = read onluy
w = write (overwrite if file exists)

"""

with open("example.txt", "w") as file:
    file.write("Hello! This is line1.\n")
    file.write("This is line 2")


file = open("example.txt", "r") 
content = file.read()

print("File Content:\n",content)
file.close()

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def save_to_file(self):
        with open("students.txt", "a") as file:
            file.write(f"{self.name}, {self.grade}\n")
        

s1 = Student("Ali", "A")
s1.save_to_file()