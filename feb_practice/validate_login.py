# You are a junior developer working in a small start-up. Your managers have asked you to develop a new account registration system for a mobile app. The system must validate user input on the sign-up form before creating an account.

# The previous junior developer wrote some helper functions that validate the name, email, and password. Use these functions to register users, store their data, and implement some error handling! These have been imported into the workspace for you. They will be a great help to you when registering the user, but first you have to understand what the function does! Inspect the docstrings of each of the helper functions: validate_name, validate_email and validate_password.

# Helper funciont



# Complete the solve function below.
def solve(s):
    split_name = s.split()
    lst = []
    for i in split_name:
        lst.append(i.capitalize())
    result = ' '.join(lst)
    print(result)
        
if __name__ == '__main__':
    s = input()
    solve(s)
