# Day 1 Project: Hello World with User input
"""
Goal
-learn hot to print output
- learn how to take input from the user
- Practice basic systax and running Python code
"""

# Project Description
# 1. Ask the user for their name
# 2. Ask the user for their age
# 3. Print a friendly message using their name and age

name : str = (input("What's your name? : ")).capitalize()
try:
    age: int = int(input("How old are you? : "))
    print(f"Hello {name}! You're {age} years old: That's great and welcome to programming: You'll be {age+1} years old next year")
except ValueError:
    print('Age should be the number!')
# for i in range(3):
