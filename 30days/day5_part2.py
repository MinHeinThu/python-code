import string
import random as rd

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

user_input = int(input('How many characters do you want in your password? '))
while True:
    try:
        characters_number = int(user_input)
        if characters_number < 8:
            print('Your number should be at least 8.')
            user_input = int(input('Please, Enter your number again: '))
        else:
            break
    except ValueError:
        print('Please, Enter numbers only.')

rd.shuffle(s1)
rd.shuffle(s2)
rd.shuffle(s3)
rd.shuffle(s4)

part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))

result = []
for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])
rd.shuffle(result)

password = ''.join(result)
print('Strong Password: ', password)

with open('p.txt', 'a') as file:
    file.write('\n')
    file.write(password)