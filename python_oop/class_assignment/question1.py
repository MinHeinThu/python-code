# Name: Min Hein Thu
# ID: 67111391
# Course: Object Oriented Programming

# Object-Oriented Programming (OOP) Class  Assignment 
# Question 1: Object-Oriented Banking System 
# You are required to develop a banking system simulation using Object-Oriented Programming (OOP).  The system should implement the following requirements. 
# Requirements: 
# 1. *Base Class (BankAccount)**: 
class BankAccount:
    def __init__(self,account_number, balance):
        #  - Attributes: account_number, balance 
        self.account_number = account_number
        self.balance = balance

#  - Methods: 
#  - deposit(amount): Adds the amount to the balance. 
    def deposit(self, amount):
        self.balance += amount
        return 

#  - withdraw(amount): Allows withdrawal if sufficient balance exists. 
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid input")
            return
        elif self.balance == 0 or self.balance < amount:
            print(f"Insufficient balance: {self.balance}")
            return
        else:
            self.balance -= amount
            return
        
    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_account_number = f"{self.account_number}-{other.account_number}"
            new_balance = self.balance + other.balance
            return BankAccount(new_account_number, new_balance)
        

#  - show_balance(): Prints the current balance. 
    def show_balance(self):
        print(f"Account number : {self.account_number}\nBalance: {self.balance}")
# 2. **Child Class (SavingsAccount)**: 
#  - Inherits from BankAccount. 
class SavingAccount(BankAccount):
    def __init__(self,account_number, balance, minimum_balance = 100):
        super().__init__(account_number,balance)
        #  - Additional Attribute: minimum_balance (Default: 100). 
        self.minimum_balance = minimum_balance
#  - Overridden Method: 
#  - withdraw(amount): Restricts withdrawal if balance falls below minimum balance. 
    def withdraw(self, amount):
        if amount <= self.balance:
            if (self.balance - amount) < self.minimum_balance:
                print(f"You account avaliable withdraw balance is {self.balance - self.minimum_balance}")
                return
            else:
                self.balance -= amount
                return

# 3. **Child Class (CheckingAccount)**
class CheckingAccount(BankAccount):
#  - Inherits from BankAccount. 
    def __init__(self, account_number, balance, overdraft_balance = -5000):
        super().__init__(account_number, balance)
        self.overdraft_balance = overdraft_balance
#  - Overridden Method: 
#  - withdraw(amount): Allows overdraft up to a limit of 5000. 
    def withdraw(self, amount):
        if amount > 0:
            new_balance = self.balance - amount
            if new_balance >= self.overdraft_balance:
                self.balance = new_balance
                
        
# 4. **Operator Overloading**: 
#  - Overload the `+` operator to allow merging of two accounts. 

# Test Cases: 
#  - Create objects for `SavingsAccount` and `CheckingAccount`. 
#  - Perform different transactions. 
#  - Use the `+` operator to merge two accounts and check the new balance.
# Expected Output Example: 
# ``` 
# Account Number: 101 | Balance: $5000 
# Deposit: $2000 | New Balance: $7000 
# Withdraw: $4000 | New Balance: $3000 
# Withdraw: $2900 | Insufficient balance! 
# Account Number: 102 | Balance: $8000 
# Overdraft Used! Withdraw: $10000 | New Balance: -$2000 
# Merged Account Balance: $1000 
# ```

saving = SavingAccount(101, 5000) 
saving.deposit(2000)
saving.show_balance()
saving.withdraw(4000)
saving.show_balance()
saving.withdraw(2900)
saving.show_balance()

checking = CheckingAccount(102, 8000)
checking.show_balance()
checking.withdraw(10000)
checking.show_balance()

merged_account = saving.__add__(checking)
merged_account.show_balance()
