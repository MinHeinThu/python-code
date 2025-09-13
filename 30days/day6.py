# Password generator
# Generate strong random passwords.
# Options: length, include/exclude numbers, symbols, uppercase, etc.
# Bonus: Save passwords into a file.

import string, random

p1 = list(string.ascii_uppercase)
p2 = list(string.ascii_lowercase)
p3 = list(string.digits)
p4 = list(string.punctuation)

length_password = int(input('Enter the length of password: '))
