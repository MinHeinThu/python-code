class Human:
    # instructur 
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # Methods
    def show_details(self):
        print(f'Name: {self.name}, Age: {self.age}')

    def __str__(self):
        return f'Name:{self.name}, Age:{self.age}'


# Creating objects

person1 = Human('Alice', 24, 'Female')
person2 = Human('Bob', 30, 'Male')

print(person1.gender)
print(person2.age)

person1.show_details()

print(str(person1))

print(id(person1))
print(person1)

