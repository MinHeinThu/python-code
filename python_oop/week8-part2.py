# Inheritance Example : Car Is-A Vehicle

class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # common attribute for all vihecles

    def move(self):
        print(f"{self.brand} is moving on the road")

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, plate_number):
        super().__init__(brand) # call parent constructor
        self.plate_number = plate_number # Car-specific attribute

    def show_info(self):
        print(f"Car Brand: {self.brand}, Plate Number: {self.plate_number}")

class City:
    def __init__(self, name, population):
        self.name = name # City has its own identity
        self.population = population
    
class Rider:
    def __init__(self, name, city):
        self.name = name 
        self.city = city # Rider has-a City (Aggregation)
    
    def show_location(self):
        print(f"Rider name: {self.name}")
        print(f"City: {self.city.population}")

class Driver:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Driver Name: {self.name}")

class Trip:
    def __init__(self, driver, rider, car):
        self.driver = driver
        self.rider = rider 
        self.car = car

    def start_trip(self):
        print("\n--- Trip Started ---")
        self.driver.show_info()
        self.rider.show_location()
        self.car.show_info()
        self.car.move()
        print("-- Trip End ---\n")

# Step 1: Create a City
bangkok = City("Bangkok", 1000000)

# Step 2: CReate A Rider and assgn a City
rider = Rider("Ali", bangkok)

# Step 3: Create a Driver
driver = Driver("Ahmed")

# Step 4: Create a car (brand + plate number)
car = Car("Toyota", "ABC-123")

# Step 5: Create a Trip
trip = Trip(driver, rider , car)

# Step 6: Start the Trip ( use all infoe)
trip.start_trip()
