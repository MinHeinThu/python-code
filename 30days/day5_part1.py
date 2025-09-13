import string
import random as rd

print('Password length must be at least 8')
length = int(input('Enter password length: '))

if length >= 8:

    print('''Choose character set for password from these :
        1. Digits
        2. Uppercase letter
        3. Lower letter
        4. Special characters
        5. Exit''')
    
    characterList = ''
    while (True):
        try:
            choice = int(input('Pick a number: '))
            if (choice == 1):
                characterList += string.digits
            elif (choice == 2):
                characterList += string.ascii_uppercase
            elif (choice == 3):
                characterList += string.ascii_lowercase
            elif (choice == 4):
                characterList += string.punctuation
            elif (choice == 5):
                break
            else:
                print("Please pick a valid option!")
        except ValueError:
            print("You pick is not number")
    password = []
    for i in range(length):
        randomchar = rd.choice(characterList)
        password.append(randomchar)

    print('The random password is ' + ''.join(password))
else:
    print('Password length is invalid')

"""
Documentation: In this password ganerator is reference to the gforg

The way I understand is for this password generator is: 
1. First we choice the length 
2. We choice what will contain our passwrod like character, digits, special character
3. After choicing everything generate random pick up to our choicing length and apppend it to the password list
4. Finally we got the list and use .join() function and got real strin password
"""