class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age")

p = Person("Alice", 25)
print(p.get_age())
p.set_age(30)
p.set_age(-5)