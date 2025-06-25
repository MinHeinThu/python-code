class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance,int) and new_balance > 0:
            self.__balance += new_balance
        else:
            print("Balance cannot be negative or string")

account = BankAccount(400)

print(account.balance)
account.balance = 500
print(account.balance)