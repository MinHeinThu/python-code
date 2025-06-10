class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    def _withdraw(self, amount):
        self._balance  -= amount
        print(f'Withdrawn: {amount}')
        print(f'New Balance: {self._balance}')

class SavingsAccount(BankAccount):
    def withdraw_money(self, amount):
        print("Precesssing withdrawal...")
        self._withdraw(amount)
        print('Transaction Complete')

savings = SavingsAccount(1000)
savings.withdraw_money(300)