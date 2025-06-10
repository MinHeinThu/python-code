class Projec:
    def __init__(self, name):
        self.name = name

class Developer:
    def __init__(self, name, project_name):
        self.name = name
        self.project_name = project_name
    
    def show_details(self):
        print(f"Developer: {self.name}")
        print(f"Project: {self.project_name.name}")

project = Projec("E-commerce Website")
dev = Developer("Ayesha", project)
dev.show_details()