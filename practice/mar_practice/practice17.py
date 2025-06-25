class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    # Getter method
    def get_age(self):
        print(f'{self.__name} is {self.__age} years old')

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Age must be positive')

person1 = Person('Jack', 33)
person1.get_age()
person1.set_age(30)
person1.get_age()