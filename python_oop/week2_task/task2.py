# Name: Min Hein Thu
# ID: 67111391
# Task 2: Banking System (Single Inheritance & Method Overriding)

# Objective:
# Create a BankAccount class (Parent)
# Create a SavingsAccount class (Child) that inherits from BankAccount
# Override the withdraw() method in SavingsAccount
# Use super() to call the parent method

# Parent class
# Define a BankAccount class:
class BankAccount:
    # Constructor
    # Attributes: account_number, balance
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    # Method 1
    # deposit(amount): Adds money to balance
    def deposit(self, amount):
        self.balance += amount
        return
    # Method 2
    # withdraw(amount): Deducts money (if sufficient balance)
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid input")
            return
        elif self.balance == 0 or self.balance < amount:
            print('Insufficient balance: {:.5f}$'.format(self.balance))
            return
        else:
            self.balance -= amount
            return
    # Method 3
    # show_balance(): Displays balance
    def show_balance(self):
        print('Account Balance: {:.5f}$'.format(self.balance) )

# Define a SavingsAccount class:
# Inherit from BankAccount
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance):
        # Use super() to reuse the parent method
        super().__init__(account_number, balance)

    # Prevents withdrawal if balance falls below $100 minimum.
    # Override withdraw(amount):
    def withdraw(self, amount):
        if amount <= 0:
            print('Invalid input')
            return
        elif  self.balance < 100 or self.balance < amount:
            print('Insufficient balance: {:.5f}$\nAccount balance minimum required is 100$'.format(self.balance))
        else:
            self.balance -= amount
            return


# Create objects and test deposit and withdrawal.
# Object
acc1 = SavingAccount(10101, 20)
# Deposit 80$
acc1.deposit(80)
# Look acc balance
acc1.show_balance()
# Withdraw 80$
acc1.withdraw(80.24)
# Look acc balance
acc1.show_balance()
# Withdraw again but failed because acc balance required minimum 100$
acc1.withdraw(10)
# if Withdraw negative or zero is input invalid
acc1.withdraw(-990)

# Deposit 80$
acc1.deposit(800)
# Look acc balance
acc1.show_balance()