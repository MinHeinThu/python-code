from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print('The engine is starting')
car = Car()

car.start_engine()


for i in range(1,1,5):
    if i % 2 == 0:
        print("hello")