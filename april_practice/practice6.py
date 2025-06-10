class Circle: 
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142* self.radius ** 2
    
    @staticmethod
    def describe():
        return "This class represnt a Circle"
    
# print(Circle(4).describe())

circle1 = Circle(6)
print(circle1.area())
print(circle1.describe())

# 🧪 Mini Practice Challenge:

# Create a TemperatureConverter class with:
# A static method: toFahrenheit(celsius: number)
# Another static method: toCelsius(fahrenheit: number)
# Want to do it in Python, TypeScript, or both?
# Or should I show the solution directly first?

class TemperatureConverter:
    # def __init__(self, number):
    #     self.number = number

    @staticmethod
    def celsiusToFahrenheit(number):
        formula1 = (number * 9 / 5) + 32
        return f"Celsius {number} is Fahrenheit {formula1}"
    
    @staticmethod
    def fahrenheitToCelsius(number):
        formula1 = (number - 32) * 5/9
        return f"Fahrenheit {number} is Celsius {formula1}"
    
print(TemperatureConverter.celsiusToFahrenheit(30))
print(TemperatureConverter.fahrenheitToCelsius(30))
        
