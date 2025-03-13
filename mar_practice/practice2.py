from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def loan_interest(self):
        pass

class HBL(Bank):
    def loan_interest(self):
        return "HBL loan interrest rate is 7%"
    
class Meezan(Bank):
    def loan_interest(self):
        return "Meezan Bank follows Islamic banking principles."
    
hbl = HBL()

meezan = Meezan()
print(hbl.loan_interest())
print(meezan.loan_interest())


