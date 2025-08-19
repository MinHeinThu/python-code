"""Day 3 Project: Number Guessing Game 🎯
Goal:
Practice while loops
Use random module
Combine conditions (if/else) with loops
Learn how to give hints to the user
Project Description:
Generate a random number between 1 and 50.
Ask the user to guess the numb
If the guess is too high → print "Too high!".
If the guess is too low → print "Too low!".
If the guess is correct → print "You got it in X tries!" and exit.
Keep track of how many attempts the user makes.
"""
import random

print('Hint: Guess the number from 1 to 50')
random_int = random.randint(1, 50)
attempts = 1
while True:
        guess = int(input('Guess the number: '))
        if guess <= 50 and guess >=1:
            if attempts < 5:
                if guess > random_int:
                    print('Too high!')
                    attempts += 1
                elif guess < random_int:
                    print('Too low!')
                    attempts += 1
                else:
                    print('🏆Yay, You win🎉')
                    print(f'You got it {attempts} tries!')
                    break
            else:
                 print('You reached limit')
                 print(f'The correct number was {random_int}')
                 break
        else:
             print('You guess is not valid')
                

