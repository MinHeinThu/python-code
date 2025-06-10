# Function to variable


def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5))

# Define fun inside other function
def add_one(number):
    def plus_one(number):
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(7))

# Passing fun as arg to other fun

def function_call(function):
    number_to_add = 2

    return function(number_to_add)

print(function_call(plus_one))

# Fun return other fun

def hello_fun():
    def say_hi():
        return 'Hi'
    return say_hi

hello = hello_fun()
print(hello())

def print_hello(message):
    print("hi there!")
    message()
    return
   

@print_hello
def greeting():
    print("How are you?")

greeting

def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@ simple_decorator
def greet():
    print("Hey! What's up?")

greet()


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

@uppercase_decorator
def say_greeting():
    return "Tarlizwa"

print(say_greeting())

# decorate = uppercase_decorator(say_greeting)
# print(decorate())

# Applygint multiple decorators to single function

import functools

def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func = function()

        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string
@uppercase_decorator
def say_something():
    return "Hello, how's is goning?"

print(say_something())