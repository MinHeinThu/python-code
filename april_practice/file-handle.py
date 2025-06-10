"""
Mode	Description
'r'	Read (default); file must exist
'w'	Write; creates or overwrites
'a'	Append; adds at end if exists
'x'	Exclusive create; fails if exists
'b'	Binary mode
't'	Text mode (default)
"""

# read() function - reads entire file
file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close() # We need to use clsee()

# readline() - this function line by line so what if you want to read all line we use readlines
# line1 = file.readline()
# line2 = file.readline()
# print(line1, line2)

lines = file.readlines()
print(lines)
file.close()

file2 = open("example.txt", "w")

file2.write("Accommondate\n")
file2.write("Abstract, accuracy\n")
file2.close()

