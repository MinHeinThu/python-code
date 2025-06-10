class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance += new_balance
            return
        else:
            print('Balance cannot be negative')

account1 = BankAccount(500)
print(account1.balance)
account1.set_balance = 4500
print(account1.balance)