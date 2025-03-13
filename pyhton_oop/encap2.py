class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f'New Balance: {self.__balance}')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Remaining Balance: {self.__balance}')
        else:
            print("Insufficient Funds")


acc = BankAccount(5000)
acc.deposit(2000)
acc.withdraw(3000)
# print(acc.__balance)