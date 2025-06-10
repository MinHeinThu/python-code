# Name: Min Hein Thu
# ID: 67111391
# Task 3: Smart Devices (Multiple Inheritance)

# Objective:
# Implement Multiple Inheritance
# Create a Device class with power_on() and power_off()
# Create a Device class:
class Device:
    # Method: power_on(), power_off()
    def power_on(self):
        print("Power is On")
    def power_off(self):
        print("Power is Off")
# Create a Camera class with capture_photo()
# Create a Camera class:
class Camera:
    # Method: capture_photo()
    def capture_photo(self):
        print("Can take a photo")
# Create a Smartphone class that inherits from both
# Create a Smartphone class
# Inherit from both Device and Camera
class Smartphone(Device, Camera):
    # Implement super() if needed
    # Implement show_features() method in Smartphone
    # Add show_features() method
    def show_features(self):
        print('Features of our phone:')
        super().power_on()
        super().power_off()
        super().capture_photo()


# Create objects and test methods.
phone1 = Smartphone()
phone1.show_features()