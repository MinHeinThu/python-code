class BanckAccount:
    def __init__(self, balance):
        self.__balance = balance
    

    def get_balance(self):
        return self.__balance
    

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposited: {amount}, New Balance: {self.__balance}')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrawn: {amount}, Remaining Balance: {self.__balance}')
        else:
            print('Insufficient Balance')


account = BanckAccount(5000)

print(account.get_balance())

account.set_balance(7000)
print(account.get_balance())

account.set_balance(-1000)

account.deposit(1000)
account.withdraw(2000)