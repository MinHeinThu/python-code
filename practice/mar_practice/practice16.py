# Private modifier

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        return
    
    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print("Withdraw success")
            return
        else:
            print("Insufficient balance")
        
    def show_balance(self):
        print(f'Account balance: {self.__balance}')


bank = BankAccount(200)
bank.show_balance()

bank.deposit(5000)
bank.show_balance()

bank.withdraw(5200)

bank.withdraw(100)
bank.show_balance()
print(bank.__balance)