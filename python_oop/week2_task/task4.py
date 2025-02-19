# Name: Min Hein Thu
# ID: 67111391
# Task 4: Food Ordering System (Hierarchical Inheritance & Method Overriding)
# Objective:
# Implement Hierarchical Inheritance
# Create a FoodItem class (Parent)
# Create Pizza and Burger (Child classes)
# Override show_details() in child classes
# Instructions:
# Create a FoodItem class:
class FoodItem:
    # Attributes: name, price
    def __init__(self, name, price):
        self.name = name
        self.price = price
    # Method: show_details()
    def show_details(self):
        print(f'{self.name} is {self.price}$')
# Create Pizza and Burger classes:
# Inherit from FoodItem
class Pizza(FoodItem):
    # Add size for Pizza
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    # Override show_details()
    def show_details(self):
        super().show_details()
        print(f"The pizza size is {self.size}")
# Inherit from FoodItem
class Burger(FoodItem):
    # Add has_cheese for Burger
    def __init__(self, name, price, has_cheese):
        super().__init__(name, price)
        self.has_cheese = has_cheese
    # Override show_details()
    def show_details(self):
        super().show_details()
        print(f"Has cheese is {self.has_cheese}")

pizza1 = Pizza('P',15,20)
burger1 = Burger('B', 3, True)
pizza1.show_details()
burger1.show_details()




# Create objects and test the show_details() method.

