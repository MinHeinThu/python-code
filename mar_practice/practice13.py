from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     @abstractmethod
#     def sleep(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"
    
#     def sleep(self):
#         return "Dog is sleeping..."
    
# dog1 = Dog()
# print(dog1.make_sound())

# class Bank(ABC):
#     @abstractmethod
#     def loan_interest(self):
#         pass

# class HBL(Bank):
#     def loan_interest(self):
#         print("HBL loan interest rate is 7%")

# class Meezan(Bank):
#     def loan_interest(self):
#         print("Meezan loan interest rate is 0% because it follows Islamic banking system")

# hbl = HBL()
# hbl.loan_interest()

# meezan = Meezan()
# meezan.loan_interest()

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
            print("Balance cannot be negative")

account = BankAccount(5000)

print(account.balance)
