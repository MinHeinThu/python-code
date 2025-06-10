# Private

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     # Getter method (to access balance outside)
#     def get_balance(self):
#         return self.__balance
    
# acc = BankAccount(50000)
# print(acc.get_balance())

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative!")


acc = BankAccount(5000)

print(acc.balance)

acc.balance = 7000

print(acc.balance)

acc.balance = -2