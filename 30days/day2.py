# Flag = True
# while True:
#     try:
#         num1 = int(input('Enter first number: '))
#         num2 = int(input('Enter second number: '))
#         operator = str(input('Enter operatin (+, -, *, /): '))
#         if operator == '+':
#             print(num1 + num2)
#         elif operator == '-':
#             print(num1 - num2)
#         elif operator == '*':
#             print(num1 * num2)
#         elif operator == '/':
#             print(num1 / num2)
#         else:
#             print(f'Invalid operator: {operator}')
        
#     except ValueError:
#         print('Your input values is wrong')
#     except ZeroDivisionError:
#         print('Cannot dividedy by zero')

#     request = input('Do you want to continue? (y/n): ')
#     if request.lower() == 'y':
#         continue   # restart loop
#     elif request.lower() == 'n':
#         print('👋 Goodbye!')
#         break      # exit loop
#     else:
#         print('⚠️ Invalid choice, exiting.')

    
while True:
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        operator = str(input('Enter operation (+, -, *, /): '))
        
        if operator == '+':
            print(num1 + num2)
        elif operator == '-':
            print(num1 - num2)
        elif operator == '*':
            print(num1 * num2)
        elif operator == '/':
            print(num1 / num2)
        else:
            print(f'Invalid operator: {operator}')
        
        # This part needs to be indented to be inside the try block
        request = input('Do you want to continue? (y/n): ')
        if request.lower() == 'y':
            continue   # restart loop
        elif request.lower() == 'n':
            print('👋 Goodbye!')
            break      # exit loop
        else:
            print('⚠️ Invalid choice, exiting.')
            break
            
    except ValueError:
        print('Your input values is wrong')
    except ZeroDivisionError:
        print('Cannot divide by zero')