# class Student:
#     def __init__(self, name, marks):
#         if marks < 0:
#             raise ValueError("Marks can\'t be negative")
#         self.name = name
#         self.marks = marks

# try:
#     s1 = Student("Ali", -30)
# except ValueError as e:
#     print("Error:", e)

# class InvalidMarksError(Exception):
#     pass

# class Student:
#     def __init__(self, name, marks):
#         if marks < 0:
#             raise InvalidMarksError("Marks must be 0 or higher")
#         self.name = name
#         self.marks = marks

# try: 
#     s1 = Student("Sara", -20)

# except InvalidMarksError as e:
#     print("Custom Error:", e)


# class InvalidMarks(Exception):
#     pass

# class ReportCard:
#     def __init__(self, name, marks):
#         if marks < 0 or marks > 100:
#             raise InvalidMarks("Marks should be between 0 and 100")
#         self.name = name
#         self.marks = marks

# try:
#     name = input("Enter student name: ")
#     marks = int(input("Enter makrs: "))
#     student = ReportCard(name, marks)
# except InvalidMarks as e:
#     print("Error:", e)
# except ValueError:
#     print("Please enter numeric value for marks")



# class OverbookingError(Exception):
#     pass

# class Hotel:
#     def __init__(self, total_rooms = 5):
#         self.available_rooms = total_rooms

#     def book_room(self, count):
#         if count > self.available_rooms:
#             raise OverbookingError("Not enough room available")
#         self.available_rooms -= count
#         print(f"{count} room(s) booked. {self.available_rooms} remaining")

# hotel = Hotel()

# try:
#     rooms = int(input("how many roooms would you like to book? "))
#     hotel.book_room(rooms)
# except OverbookingError as e:
#     print("Booking failed:", e)
# except ValueError:
#     print("Invalid input")


class InvalidPIN(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
    
    def withdraw(self, entered_pin, amount):
        if entered_pin != self.pin:
            raise InvalidPIN("Wrong PIN entered.")
        
        if amount > self.balance:
            raise InsufficientBalance("Not enough balance.")
        
        self.balance -= amount
        print(f"Withdrawn: {amount}, Remaining balance: {self.balance}")

atm = ATM (pin=1234, balance=1000)

try:
    entered_pin = int(input("Enter your PIN: "))
    amount = int(input("Enter amount to withdraw: "))
    atm.withdraw(entered_pin, amount)

except InvalidPIN as e:
    print(e)
except InsufficientBalance as e:
    print(e)
except ValueError:
    print("Please enter valid numeric input.")