from abc import abstractmethod, ABC

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return 'Car is starting engine'
    
car = Car()
print(car.start_engine())
