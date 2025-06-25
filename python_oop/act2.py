class CPU:
    def process(self):
        print("CPU processing")

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        self.cup.process()
        print("Computer is running")

com1 = Computer()
com1.run()

# class Engine:
#     def start(self):
#         print("Engine starts")

# class Car:
#     def __init__(self):
#         self.engine = Engine()  # Composition

#     def drive(self):
#         self.engine.start()
#         print("Car drives")

# car = Car()
# car.drive()
