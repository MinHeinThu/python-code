import random

print('Welcome CLI Rock, Paper, Scissors Game')
choices = ['rock', 'paper', 'scissors']

while True:
    # try:
    #     hand_shape = str(input('Choose: [rock, paper, scissors]: '))
    #     shape = ['rock', 'paper', 'scissors']
    #     if hand_shape in shape:
    #         user = hand_shape
    #         bot = random.choice(shape)
    #         print(f'Player chose: {user}, Bot chose: {bot}')
    #         if bot == user:
    #             print("It's a tie!")
    #         elif (user == 'rock' and bot == 'sissors') or (user == 'paper' and bot == 'rock') or (user == 'scissors' and bot == 'paper'):
    #             print('Player wins: 🏆')
    #         else:
    #             print('Bot wins: 🏆')
    #     else:
    #         print('Input invalid')
    # except ValueError:
    #     print('Input invalid')

    user_choice = input('Enter rock, paper, scissors: ').lower()
    if user_choice not in choices:
        print('Invalid choice. Please choose rock, paper, or scissors')
    computer_choice = random.choice(choices)
    print(f'Player choice: {user_choice}, Computer choice: {computer_choice}')
    if user_choice == computer_choice:
        print("It's a tie")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        print('Player win!')
    else:
        print('Computer win')
    play_again = input('Play again? y/n: ').lower()
    if play_again == 'n':
        print('Goodbye! Thanks for playing')
        break
    elif play_again == 'y':
        continue
    else:
        print('Only answer y/n')