import string
import random as rd

# First I will make sure how many length of password should I choose

p1 = list(string.ascii_uppercase)
p2 = list(string.ascii_lowercase)
p3 = list(string.digits)
p4 = list(string.punctuation)

while True:
    try:
        length_of_password = int(input('Enter the length of password: '))
        if length_of_password < 8:
            print('Password length must be more than 8')
            length_of_password = int(input('Enter the lenght of passwrd: '))
        else:
            break
    except ValueError:
        print('Length of passwrod should be number')

rd.shuffle(p1)
rd.shuffle(p2)
rd.shuffle(p3)
rd.shuffle(p4)

# This part is calculate how we make our random password shold be like how many upper and lower case should be contain and digits and punction cointain
part1 = round(length_of_password * (80 / 100))
part2 = round(length_of_password * (20 / 100))

password = []

for i in range(part1):
    password.append(p1[i])
    password.append(p2[i])

for i in range(part2):
    password.append(p3[i])
    password.append(p4[i])

# Generated password is list to make staring I use join() function
generated_password = ''.join(password)

# I store the generated password in txt file
with open('password_store.txt', 'a') as file:
    file.write('\n')
    file.write(generated_password)