# 

from re import A


class Human:

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # methods
    def __str__(self):
        return f'{self.name} is {self.age} year olds'
    
    def action(self):
        return f'{self.name} can walk , can speak'
    

h1 = Human('Jack', 22)
print(h1)

h2 = Human('Dalio', 3)
print(h2)
print(h2.action())

# Inheritance

class Baby(Human):
    def __init__(self,name, age, dog):
        super().__init__(name, age)
        self.dog = dog

    # Methods Overridding
    def action(self):
        return f'{self.name} Can walk but cannot speak'
    
    def is_owned_dog(self):
        return f'The baby {self.name.name} is own {self.dog.name.name}'
    
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} is dog'
    
d1 = Dog('Miki')
print(d1)

b1 = Baby('Miko', 1, d1)
print(b1.action())
print(b1)
print(b1.is_owned_dog)
