class Car:
    def __init__(self,speed):
        self.__speed = speed

    @property
    def get_speed(self):
        return self.__speed
    @get_speed.setter
    def set_speed(self, new_speed):
        if new_speed > 0 and new_speed <= 200:
            self.__speed = new_speed
        else:
            print("Speed out of the range")
        
car1 = Car(200)
print(f"Car is driving at speed: {car1.get_speed}")
car1.set_speed = 250
car1.set_speed = 50
print(f"Car is driving at speed: {car1.get_speed}")

