"""
Introduction to file Handling
What is file handling: File handling menas reads data from a file or writing data to a file using Pyhton code

Types of Files:
1. Text files(txt)
2. Binary Files(images, videos, audio)

'r' = Read only
'w' = Write (overwrite if file exists)
'a' = Append(add to file)
'x' = Create file, error if exists
'b' = binary mode (image, pdf)
't' = Text mode(default)
"""

# file Handling Basic Syntax

# 1. opening a file
# file = open("example.txt", "r")
# Closing a File
# file.close()

# 2. Writhing to a file
# with open("example.txt", "w") as file:
    # file.write("Hello, world")



def add(a, b):
    return a + b

print(add(2,4))