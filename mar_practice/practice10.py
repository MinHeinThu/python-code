# class MobilePhone:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def details(self):
#         print(f'The brand phone is {self.brand} the model is {self.model} and the price is {self.price}')

# phone1 = MobilePhone('Vivo', "y20", 5000)
# phone1.details()


class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dogs barks")
    def speak(self):
        super().speak()
        print("hee")

d1 = Dog()
d1.speak()
d1.bark()