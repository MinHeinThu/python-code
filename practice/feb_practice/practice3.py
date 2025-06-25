# Method overloading 
# Compile time polymorphism

# Default argument

def add(a, b, c = 0):
    return a + b + c

print(add(1, 3, 4))

# Using *args and **kwargs

def add(*args):
    return sum(args)

print(add(2,3,5,5,5))

print(type(add))

def key_value(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

key_value(name = "min", age = 1, major = "Hein")
