from abc import ABC, abstractmethod

class Order(ABC):

    def place_order(self):
        print("Order placed successfully")

    @abstractmethod
    def process_paying(self, amount):
        pass

    @abstractmethod
    def calculate_delivery_charges(self):
        pass


class NormalOrder(Order):
    def process_paying(self,amount):
        print(f"Normal one: {amount}")

    def calculate_delivery_charges(self):
        print(f"Normal: 5$")

    


class ExpressOrder(Order):
    def process_paying(self, amount):
        print(f"Express: {amount}")

    def calculate_delivery_charges(self):
        print(f"Express: 15$")

n = NormalOrder()
n.process_paying(15)
n.place_order()
n.calculate_delivery_charges()