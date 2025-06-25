class School:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"The School Name: {self.name}"
    
school = School("Krirk University")

print(school.get_info())

# 2. Abstract Class: Person
from abc import ABC, abstractmethod
# -Inherit from ABC (from abc module)
class Person(ABC):
    def __init__(self, name: str, email: str, contact: str):
        self.name = name
        self._email = email
        self.__contact = contact
# - Attributes:
# -name (string)
# email (protected)
# contact (private)

# - Methods:

# -set contact(contact) - validates that the contact number is exactly 11 digits. Raise a ValueError
    def set_contact(self, contact):
        if len(contact) == 11:
            self.__contact = contact
        else:
            raise ValueError("contact must be 11 digits")
        
    @property
    def get_contact(self):
        return self.__contact

# if invalid

# contact-use the @property decorator to access the private contact

# -show role()-abstract method to be implemented by subclasses
    @abstractmethod
    def show_role(self):
        pass

# person1 = Person("ja", "something@email", "00938474743")

