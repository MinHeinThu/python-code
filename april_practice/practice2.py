class CPU:
    def process(self):
        print("CPU processing...")
    
# This one is composition
class Computer:
    def __init__(self):
        self.cpu = CPU()
    def run(self):
        self.cpu.process()
        print("Coumputer is running")
    
com = Computer()
com.run()


# This one is using aggregration
class Project:
    def __init__(self, name):
        self.name = name

class Developer:
    def __init__(self, name , reference_project):
        self.name = name
        self.reference_project = reference_project

    def show_details(self):
        print(f"Developer: {self.name}\nProject: {self.reference_project.name}")
    
project1 = Project("E-commerce Website")
developer1 = Developer("ayesha", project1)

developer1.show_details()