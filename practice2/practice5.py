class Person:
    def __init__(self, first_name, last_name, age, date_of_birth):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age: str = age
        self.__date_of_birth: str = date_of_birth
    
    def __str__(self):
        return f'{self.__first_name +' '+self.__last_name} is {self.__age}'

person1 = Person('Jack', 'Jack', 22, '2201')
print(person1)

sett = {1, 2, 3, 4, 5}
print(sett)