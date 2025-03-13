class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    # @balance.setter
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")

account = BankAccount(5000)

print(account.balance)

account.balance = 7000
print(account.balance)

account.balance = -1000
